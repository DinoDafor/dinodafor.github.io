#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка английской версии сайта в папку en/.

Русские HTML-файлы — источник правды. Скрипт проходит по ним,
подменяет тексты по словарю из translations.py, чинит относительные
ссылки и складывает результат в en/.

Запуск:   python3 build.py
Проверка: python3 build.py --check   (только показать непереведённое)

После правки русского текста запустите сборку заново,
иначе английская версия останется старой.
"""
import json
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://dinodafor.github.io/'
OUT = 'en'

# атрибуты, содержимое которых видит пользователь
TEXT_ATTRS = {'alt', 'placeholder', 'title', 'aria-label', 'value', 'content', 'data-prefix'}
# атрибуты со ссылками
LINK_ATTRS = {'href', 'src'}
# meta, которые переводить не нужно
SKIP_CONTENT = {'width=device-width, initial-scale=1', 'utf-8'}

CYRILLIC = re.compile('[а-яА-ЯёЁ]')

RATE_FILE = os.path.join(BASE, 'rate.json')
RATE_API = 'https://www.cbr-xml-daily.ru/daily_json.js'
RATE_FALLBACK = 95.0


def fetch_rate():
    """Курс доллара у ЦБ. Если не ответил — берём прошлый, потом запасной.

    Сборка не должна падать из-за чужого сервера: цены просто
    останутся такими, какими были в прошлый раз.
    """
    try:
        import urllib.request
        with urllib.request.urlopen(RATE_API, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
        value = float(data['Valute']['USD']['Value'])
        date = data['Date'][:10]
        json.dump({'usd': round(value, 4), 'date': date, 'source': 'ЦБ РФ'},
                  open(RATE_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('курс ЦБ на %s: 1 $ = %.2f ₽' % (date, value))
        return value, date
    except Exception as error:                       # noqa: BLE001 — причина не важна
        print('курс не получен (%s), берём сохранённый' % error)

    if os.path.exists(RATE_FILE):
        saved = json.load(open(RATE_FILE, encoding='utf-8'))
        print('сохранённый курс на %s: 1 $ = %.2f ₽' % (saved['date'], saved['usd']))
        return float(saved['usd']), saved['date']

    print('курс не найден совсем, берём запасной: %.2f' % RATE_FALLBACK)
    return RATE_FALLBACK, ''


USD_RATE, USD_RATE_DATE = fetch_rate()


def usd(rub):
    """Рубли в доллары — той же арифметикой, что и в script.js."""
    return '{:,}'.format(int(round(rub / USD_RATE / 10) * 10))

try:
    from translations import STRINGS
except ImportError:                                    # первый запуск
    STRINGS = {}

missing = []


def tr(text, where=''):
    """Перевод строки. Незнакомое — запоминаем и оставляем как есть."""
    key = ' '.join(text.split())
    if not key or not CYRILLIC.search(key):
        return text
    if key in STRINGS:
        # сохраняем ведущие и завершающие пробелы исходника
        lead = text[:len(text) - len(text.lstrip())]
        tail = text[len(text.rstrip()):]
        return lead + STRINGS[key] + tail
    if key not in missing:
        missing.append(key)
    return text


def rewrite_link(value, ru_rel):
    """Ссылку из русской страницы приводим к виду для страницы в en/."""
    if not value or value.startswith(('http', 'mailto:', 'data:', '#', 'tel:')):
        return value

    parts = urlsplit(value)
    if not parts.path:
        return value

    ru_dir = os.path.dirname(ru_rel)
    en_dir = os.path.join(OUT, ru_dir) if ru_dir else OUT
    target = os.path.normpath(os.path.join(ru_dir, parts.path))

    if parts.path.endswith('/'):                        # ссылка на папку
        target = os.path.join(target, '')

    is_page = target.endswith('.html') or parts.path.endswith('/')
    if is_page:
        new_target = os.path.join(OUT, target)
    else:
        new_target = target                              # картинки, стили, скрипты

    rel = os.path.relpath(new_target, en_dir)
    if parts.path.endswith('/') and not rel.endswith('/'):
        rel += '/'
    return urlunsplit(('', '', rel, parts.query, parts.fragment))


def translate_jsonld(raw, ru_rel):
    def walk(node):
        if isinstance(node, dict):
            return {k: walk(v) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v) for v in node]
        if isinstance(node, str):
            if node.startswith(SITE):
                tail = node[len(SITE):]
                return SITE + (OUT + '/' + tail if tail else OUT + '/')
            return tr(node, 'json-ld')
        return node

    return json.dumps(walk(json.loads(raw)), ensure_ascii=False, indent=2)


class Builder(HTMLParser):
    def __init__(self, ru_rel):
        super().__init__(convert_charrefs=False)
        self.ru_rel = ru_rel
        self.out = []
        self.stack = []
        self.in_ldjson = False
        self.in_code = False
        self.in_lang_switch = False
        self.money = None

    # --- служебное ---
    def emit(self, text):
        self.out.append(text)

    def attrs_to_str(self, tag, attrs):
        result = []
        classes = dict(attrs).get('class', '') or ''

        for name, value in attrs:
            if value is None:
                result.append(' ' + name)
                continue

            if tag == 'html' and name == 'lang':
                value = 'en'
            elif name in LINK_ATTRS:
                if 'switch__lang' in classes and name == 'href':
                    # обратная ссылка на русскую версию
                    en_dir = os.path.join(OUT, os.path.dirname(self.ru_rel))
                    value = os.path.relpath(self.ru_rel, en_dir)
                else:
                    value = rewrite_link(value, self.ru_rel)
            elif 'switch__lang' in classes and name in ('hreflang', 'lang'):
                value = 'ru'
            elif name in TEXT_ATTRS and value not in SKIP_CONTENT:
                value = tr(value, tag + '@' + name)

            result.append(' %s="%s"' % (name, value.replace('"', '&quot;')))

        return ''.join(result)

    # --- обработчики парсера ---
    def handle_decl(self, decl):
        self.emit('<!%s>' % decl)

    def handle_starttag(self, tag, attrs):
        self.emit('<%s%s>' % (tag, self.attrs_to_str(tag, attrs)))
        self.stack.append(tag)
        d = dict(attrs)
        if tag == 'a' and 'switch__lang' in (d.get('class') or ''):
            self.in_lang_switch = True
        if 'money' in (d.get('class') or '').split():
            self.money = d
        if tag == 'script' and d.get('type') == 'application/ld+json':
            self.in_ldjson = True
        if tag in ('script', 'style', 'code', 'pre'):
            self.in_code = True

    def handle_startendtag(self, tag, attrs):
        self.emit('<%s%s>' % (tag, self.attrs_to_str(tag, attrs)))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        if tag in ('script', 'style', 'code', 'pre'):
            self.in_code = False
        self.in_ldjson = False
        self.emit('</%s>' % tag)

    def handle_data(self, data):
        if self.money is not None:
            # цену не переводим, а пересчитываем: en/ живёт в долларах
            low = usd(int(self.money['data-rub']))
            high = self.money.get('data-rub-max')
            text = '$' + low + ('–' + usd(int(high)) if high else '')
            if self.money.get('data-prefix'):
                text = 'from ' + text
            self.emit(text)
            self.money = None
        elif self.in_lang_switch:
            self.emit(data.replace('EN', 'RU'))   # подпись ведёт обратно на русскую версию
            self.in_lang_switch = False
        elif self.in_ldjson:
            self.emit('\n  ' + translate_jsonld(data, self.ru_rel).replace('\n', '\n  ') + '\n  ')
        elif self.in_code:
            self.emit(data)
        else:
            self.emit(tr(data, 'text'))

    def handle_comment(self, data):
        self.emit('<!--%s-->' % data)          # комментарии оставляем по-русски

    def handle_entityref(self, name):
        self.emit('&%s;' % name)

    def handle_charref(self, name):
        self.emit('&#%s;' % name)


def hreflang_block(ru_rel):
    """Ссылки-альтернативы для обеих версий."""
    ru_url = SITE + ('' if ru_rel == 'index.html' else ru_rel).replace('blog/index.html', 'blog/')
    en_url = SITE + OUT + '/' + ('' if ru_rel == 'index.html' else ru_rel).replace('blog/index.html', 'blog/')
    return ('  <link rel="alternate" hreflang="ru" href="%s">\n'
            '  <link rel="alternate" hreflang="en" href="%s">\n'
            '  <link rel="alternate" hreflang="x-default" href="%s">\n' % (ru_url, en_url, ru_url))


def build_page(ru_rel):
    src = open(os.path.join(BASE, ru_rel), encoding='utf-8').read()

    # ссылки-альтернативы в русскую версию (идемпотентно)
    block = hreflang_block(ru_rel)
    if 'rel="alternate"' not in src:
        src = src.replace('  <link rel="stylesheet"', block + '  <link rel="stylesheet"')

    # курс в мета-теге: страница знает его сразу, без запроса к API
    meta = '  <meta name="usd-rate" content="%.4f" data-date="%s">\n' % (USD_RATE, USD_RATE_DATE)
    src = re.sub(r'  <meta name="usd-rate"[^>]*>\n', '', src)
    src = src.replace('  <link rel="stylesheet"', meta + '  <link rel="stylesheet"')
    open(os.path.join(BASE, ru_rel), 'w', encoding='utf-8').write(src)

    builder = Builder(ru_rel)
    builder.feed(src)
    html = ''.join(builder.out)

    # адреса самой страницы: канонический и og:url
    depth_prefix = SITE
    for tag in ('rel="canonical" href="', 'property="og:url" content="'):
        html = html.replace(tag + depth_prefix, tag + depth_prefix + OUT + '/')
    html = html.replace('content="ru_RU"', 'content="en_US"')
    html = html.replace('hreflang="x-default" href="%s%s/' % (SITE, OUT),
                        'hreflang="x-default" href="%s' % SITE)

    out_path = os.path.join(BASE, OUT, ru_rel)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, 'w', encoding='utf-8').write(html)
    return out_path


def main():
    pages = [f for f in sorted(os.listdir(BASE)) if f.endswith('.html')]
    pages += ['blog/' + f for f in sorted(os.listdir(os.path.join(BASE, 'blog'))) if f.endswith('.html')]

    made = [build_page(page) for page in pages]

    print('собрано страниц: %d' % len(made))
    if missing:
        print('\nНЕ ПЕРЕВЕДЕНО (%d строк):' % len(missing))
        for line in missing:
            print('  ' + line)
        report = os.path.join(BASE, 'missing.txt')
        open(report, 'w', encoding='utf-8').write('\n'.join(missing))
        print('\nсписок сохранён в missing.txt')
    else:
        print('все строки переведены')


if __name__ == '__main__':
    main()
