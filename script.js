/* ============================================================
   Портфолио — минимальный ванильный JS
   1) плавное появление секций при скролле (IntersectionObserver)
   2) тонкая граница у шапки после прокрутки
   3) текущий год в подвале
   ============================================================ */

(function () {
  'use strict';

  var reduceMotion = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Английская версия лежит в en/ и собирается из русской скриптом build.py.
     Тексты, которые рождаются в JS, переводятся здесь. */
  var isEnglish = document.documentElement.lang === 'en';

  var L = isEnglish ? {
    copied: 'Copied',
    again: '↻ Again',
    want: 'I want one like this →',
    wantText: 'Hi! Writing from your website. I want a bot like the demo:',
    briefIntro: 'Hi! Writing from your website, I filled in the brief.',
    brief: ['Business', 'What to simplify', 'What is needed', 'Currently using',
            'Who will use it', 'Timeline', 'Budget', 'Also important']
  } : {
    copied: 'Скопировано',
    again: '↻ Ещё раз',
    want: 'Хочу такого же →',
    wantText: 'Здравствуйте! Пишу с сайта. Хочу такого же бота:',
    briefIntro: 'Здравствуйте! Пишу с сайта, заполнил бриф.',
    brief: ['Бизнес', 'Что упростить', 'Что нужно', 'Сейчас пользуются',
            'Кто пользуется', 'Сроки', 'Бюджет', 'Ещё важно']
  };

  /* ---- 1. Появление секций ---- */

  var items = document.querySelectorAll('.reveal');

  function showAll() {
    for (var i = 0; i < items.length; i++) {
      items[i].classList.add('is-visible');
    }
  }

  if (!('IntersectionObserver' in window) || reduceMotion) {
    showAll();
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -12% 0px',
      threshold: 0.12
    });

    items.forEach(function (el) { observer.observe(el); });

    // Страховка: то, что уже в первом экране, показываем сразу.
    requestAnimationFrame(function () {
      items.forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add('is-visible');
        }
      });
    });
  }

  /* ---- 2. Граница у шапки ---- */

  var header = document.querySelector('.site-header');

  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- 3. Липкая кнопка на мобильном ----
     Показываем, когда первый экран уже прокручен,
     и убираем, когда виден блок контактов: там кнопка и так есть. */

  var cookieOpen = false;   // пока висит уведомление о cookie, кнопку не показываем
  var updateCta = null;

  var cta = document.querySelector('.mobile-cta');
  var hero = document.querySelector('.hero');
  var contacts = document.getElementById('contacts');

  if (cta && hero && contacts && 'IntersectionObserver' in window) {
    var heroVisible = true;
    var contactsVisible = false;

    var update = function () {
      cta.classList.toggle('is-shown', !heroVisible && !contactsVisible && !cookieOpen);
    };
    updateCta = update;

    new IntersectionObserver(function (entries) {
      heroVisible = entries[0].isIntersecting;
      update();
    }, { threshold: 0 }).observe(hero);

    new IntersectionObserver(function (entries) {
      contactsVisible = entries[0].isIntersecting;
      update();
    }, { threshold: 0 }).observe(contacts);
  } else if (cta) {
    cta.classList.add('is-shown');
  }

  /* ---- 4. Уведомление о cookie ----
     Показываем один раз: ответ запоминаем в localStorage.
     В приватном режиме доступ к хранилищу может быть запрещён —
     поэтому обе операции обёрнуты в try/catch, и уведомление
     в худшем случае просто покажется снова. */

  var notice = document.querySelector('.cookie');

  if (notice) {
    var KEY = 'cookie-notice-accepted';
    var seen = null;

    try { seen = window.localStorage.getItem(KEY); } catch (e) { seen = null; }

    if (!seen) {
      cookieOpen = true;
      notice.hidden = false;
      void notice.offsetWidth;        // то же самое: даём браузеру исходное состояние
      notice.classList.add('is-shown');
    }

    var okButton = notice.querySelector('.cookie__ok');

    if (okButton) {
      okButton.addEventListener('click', function () {
        cookieOpen = false;
        notice.classList.remove('is-shown');

        try { window.localStorage.setItem(KEY, '1'); } catch (e) {}

        setTimeout(function () { notice.hidden = true; }, 400);
        if (updateCta) { updateCta(); }
      });
    }
  }

  /* ---- 5. Демо-бот на первом экране ----
     В разметке лежит статичный диалог — его видно без JS и при
     отключённой анимации. Если скрипт работает, лог очищается
     и запускается интерактивный сценарий: кнопки можно нажимать.

     СЦЕНАРИЙ МЕНЯЕТСЯ ЗДЕСЬ. Каждый шаг: текст бота и варианты ответа.
     {choice} в тексте подставляет то, что выбрал посетитель. */

  var scenarioEn = {
    start: {
      text: 'Hi! I am the salon bot. Shall I book you in or answer a question?',
      choices: [
        { label: 'Book me in', next: 'branch' },
        { label: 'How much is it', next: 'price' }
      ]
    },
    price: {
      text: 'Manicure from ₽1,500, pedicure from ₽2,000, polish included. Shall I book you?',
      choices: [
        { label: 'Yes, book me', next: 'branch' },
        { label: 'Thanks, later', next: 'bye' }
      ]
    },
    branch: {
      text: 'Which location works for you?',
      choices: [
        { label: 'Lenina street', next: 'time' },
        { label: 'Mira avenue', next: 'time' }
      ]
    },
    time: {
      text: 'Tomorrow is open. Pick a time:',
      choices: [
        { label: '11:00', next: 'done' },
        { label: '14:30', next: 'done' },
        { label: '18:00', next: 'done' }
      ]
    },
    done: {
      text: 'Booked you for {choice} with Olga. I will remind you 3 hours before — the booking is already in the receptionist’s spreadsheet.',
      ok: true,
      end: true
    },
    bye: {
      text: 'Have a good day! If you change your mind, I am here around the clock.',
      end: true
    }
  };

  var scenarioRu = {
    start: {
      text: 'Здравствуйте! Я бот студии. Записать вас или ответить на вопрос?',
      choices: [
        { label: 'Записаться', next: 'branch' },
        { label: 'Сколько стоит', next: 'price' }
      ]
    },
    price: {
      text: 'Маникюр — от 1 500 ₽, педикюр — от 2 000 ₽, покрытие входит. Записать?',
      choices: [
        { label: 'Да, записаться', next: 'branch' },
        { label: 'Спасибо, позже', next: 'bye' }
      ]
    },
    branch: {
      text: 'В какой филиал удобно?',
      choices: [
        { label: 'На Ленина', next: 'time' },
        { label: 'На Мира', next: 'time' }
      ]
    },
    time: {
      text: 'Завтра свободно. Выберите время:',
      choices: [
        { label: '11:00', next: 'done' },
        { label: '14:30', next: 'done' },
        { label: '18:00', next: 'done' }
      ]
    },
    done: {
      text: 'Записала вас на {choice}, мастер Ольга. Напомню за 3 часа — заявка уже у администратора в таблице.',
      ok: true,
      end: true
    },
    bye: {
      text: 'Хорошего дня! Если передумаете, я на месте круглосуточно.',
      end: true
    }
  };

  var scenario = isEnglish ? scenarioEn : scenarioRu;

  var log = document.querySelector('.chat__log');

  if (log) {
    var staticMsgs = Array.prototype.slice.call(log.children);

    var mount = function (el) {
      el.classList.add('is-mounted');
      void el.offsetWidth;            // пересчёт стилей, иначе перехода не будет
      el.classList.add('is-shown');
    };

    if (reduceMotion || !('IntersectionObserver' in window)) {
      staticMsgs.forEach(mount);
    } else {
      var lastChoice = '';

      var typing = document.createElement('li');
      typing.className = 'msg msg--out msg--typing';
      typing.innerHTML = '<i></i><i></i><i></i>';

      var addMessage = function (text, kind) {
        var li = document.createElement('li');
        li.className = 'msg ' + kind;
        li.textContent = text.replace('{choice}', lastChoice);
        log.appendChild(li);
        mount(li);
        return li;
      };

      var addChoices = function (choices) {
        var li = document.createElement('li');
        li.className = 'msg msg--chips';

        choices.forEach(function (choice) {
          var button = document.createElement('button');
          button.type = 'button';
          button.className = 'chip';
          button.textContent = choice.label;

          button.addEventListener('click', function () {
            li.parentNode && li.parentNode.removeChild(li);
            lastChoice = choice.label;
            addMessage(choice.label, 'msg--in');
            step(choice.next);
          });

          li.appendChild(button);
        });

        log.appendChild(li);
        mount(li);
      };

      var addFinish = function () {
        var li = document.createElement('li');
        li.className = 'msg msg--chips chat__finish';

        var again = document.createElement('button');
        again.type = 'button';
        again.className = 'chip';
        again.textContent = L.again;
        again.addEventListener('click', function () {
          log.innerHTML = '';
          lastChoice = '';
          step('start');
        });

        var order = document.createElement('a');
        order.className = 'chip chip--accent';
        order.href = 'https://t.me/DinoDafor?text=' + encodeURIComponent(L.wantText);
        order.textContent = L.want;

        li.appendChild(again);
        li.appendChild(order);
        log.appendChild(li);
        mount(li);
      };

      var step = function (key) {
        var node = scenario[key];
        if (!node) { return; }

        log.appendChild(typing);
        mount(typing);

        setTimeout(function () {
          if (typing.parentNode) { typing.parentNode.removeChild(typing); }
          typing.classList.remove('is-mounted', 'is-shown');

          addMessage(node.text, node.ok ? 'msg--out msg--ok' : 'msg--out');

          if (node.choices) {
            setTimeout(function () { addChoices(node.choices); }, 350);
          } else if (node.end) {
            setTimeout(addFinish, 600);
          }
        }, 900);
      };

      var chatObserver = new IntersectionObserver(function (entries, obs) {
        if (entries[0].isIntersecting) {
          obs.disconnect();
          log.innerHTML = '';       // убираем статичный запасной диалог
          step('start');
        }
      }, { threshold: 0.25 });

      chatObserver.observe(log);
    }
  }

  /* ---- 6. Валюта ----
     КУРС ЗАДАЁТСЯ ЗДЕСЬ И ОБНОВЛЯЕТСЯ РУКАМИ. Внешнее API не используется
     намеренно: оно однажды молча отвалится, и сайт покажет ерунду.
     RATES — сколько рублей в одной единице валюты. */

  var RATES = { RUB: 1, USD: 95, EUR: 103 };
  var RATE_DATE = '3 сентября 2026';
  var CURRENCY_KEY = 'currency';
  var currency = 'RUB';
  try { currency = window.localStorage.getItem(CURRENCY_KEY) || 'RUB'; } catch (e) {}
  if (!RATES[currency]) { currency = 'RUB'; }

  var calcUpdate = null;   // калькулятор подставит сюда свою перерисовку

  var spaced = function (value) {
    return String(value).replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  };

  // суммы до 10 000 округляем до сотен, иначе почасовая ставка «поедет»
  var roundRub = function (value) {
    return value >= 10000 ? Math.round(value / 1000) * 1000 : Math.round(value / 100) * 100;
  };

  // одна сумма в текущей валюте
  var formatMoney = function (rub) {
    if (currency === 'RUB') {
      return spaced(roundRub(rub)) + ' \u20BD';
    }
    var value = Math.round(rub / RATES[currency] / 10) * 10;
    return (currency === 'USD' ? '$' : '\u20AC') + spaced(value);
  };

  // диапазон: вторая сумма без знака валюты
  var formatRange = function (min, max) {
    if (currency === 'RUB') {
      return spaced(roundRub(min)) + ' – ' + spaced(roundRub(max)) + ' \u20BD';
    }
    var a = Math.round(min / RATES[currency] / 10) * 10;
    var b = Math.round(max / RATES[currency] / 10) * 10;
    return (currency === 'USD' ? '$' : '\u20AC') + spaced(a) + '–' + spaced(b);
  };

  var applyCurrency = function () {
    var nodes = document.querySelectorAll('.money');

    Array.prototype.forEach.call(nodes, function (node) {
      var min = parseInt(node.getAttribute('data-rub'), 10);
      var max = parseInt(node.getAttribute('data-rub-max'), 10);
      var prefix = node.getAttribute('data-prefix');
      var text = max ? formatRange(min, max) : formatMoney(min);

      if (prefix) { text = (isEnglish ? 'from' : prefix) + ' ' + text; }
      node.textContent = text;
    });

    var buttons = document.querySelectorAll('.switch__cur-btn');
    Array.prototype.forEach.call(buttons, function (button) {
      var active = button.getAttribute('data-cur') === currency;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });

    var notes = document.querySelectorAll('[data-rate-note]');
    Array.prototype.forEach.call(notes, function (note) {
      if (currency === 'RUB') {
        note.textContent = isEnglish
          ? 'Prices are fixed in roubles; other currencies are shown for reference.'
          : 'Итоговая сумма фиксируется в рублях, другие валюты — для ориентира.';
      } else {
        note.textContent = (isEnglish ? 'Rate as of ' : 'Курс на ') + RATE_DATE +
          ': 1 ' + currency + ' = ' + RATES[currency] + ' \u20BD. ' +
          (isEnglish ? 'The contract amount is fixed in roubles.'
                     : 'Сумма в договоре фиксируется в рублях.');
      }
    });

    if (calcUpdate) { calcUpdate(); }
  };

  var currencyButtons = document.querySelectorAll('.switch__cur-btn');

  Array.prototype.forEach.call(currencyButtons, function (button) {
    button.addEventListener('click', function () {
      currency = button.getAttribute('data-cur');
      try { window.localStorage.setItem(CURRENCY_KEY, currency); } catch (e) {}
      applyCurrency();
    });
  });

  applyCurrency();

  /* ---- 7. Калькулятор ----
     Все цены и сроки живут в data-атрибутах разметки,
     здесь только сложение и сборка сообщения для Telegram. */

  var calc = document.querySelector('.calc');

  if (calc) {
    var priceOut = document.getElementById('calc-price');
    var daysOut = document.getElementById('calc-days');
    var summaryOut = document.getElementById('calc-summary');
    var sendLink = document.getElementById('calc-send');
    var urgent = document.getElementById('calc-urgent');
    var options = Array.prototype.slice.call(calc.querySelectorAll('.calc__opt'));

    var num = function (el, name) { return parseInt(el.getAttribute(name), 10) || 0; };

    var checkedType = function () {
      return calc.querySelector('input[name="calc-type"]:checked');
    };

    // опции, не относящиеся к выбранному типу, прячем и снимаем
    var syncOptions = function (key) {
      options.forEach(function (opt) {
        var fits = opt.getAttribute('data-for').split(' ').indexOf(key) !== -1;
        opt.hidden = !fits;
        if (!fits) { opt.querySelector('input').checked = false; }
      });
    };

    var update = function () {
      var type = checkedType();
      if (!type) { return; }

      var key = type.getAttribute('data-key');
      syncOptions(key);

      var priceMin = num(type, 'data-price-min');
      var priceMax = num(type, 'data-price-max');
      var daysMin = num(type, 'data-days-min');
      var daysMax = num(type, 'data-days-max');
      var picked = [];

      options.forEach(function (opt) {
        var input = opt.querySelector('input');
        if (opt.hidden || !input.checked) { return; }
        priceMin += num(input, 'data-price-min');
        priceMax += num(input, 'data-price-max');
        daysMin += num(input, 'data-days-min');
        daysMax += num(input, 'data-days-max');
        picked.push(input.value);
      });

      var rush = urgent && urgent.checked;
      if (rush) {
        priceMin *= 1.3;
        priceMax *= 1.3;
        daysMin = Math.max(2, Math.round(daysMin * 0.7));
        daysMax = Math.max(3, Math.round(daysMax * 0.7));
      }

      priceOut.textContent = formatRange(priceMin, priceMax);
      daysOut.textContent = daysMin + '–' + daysMax +
        (isEnglish ? ' working days' : ' рабочих дней');

      summaryOut.innerHTML = '';
      picked.forEach(function (name) {
        var li = document.createElement('li');
        li.textContent = name.charAt(0).toUpperCase() + name.slice(1);
        summaryOut.appendChild(li);
      });

      var message = (isEnglish ? 'Hi! Writing from your website. ' : 'Здравствуйте! Пишу с сайта. ') +
                    type.value + '.';
      if (picked.length) {
        message += (isEnglish ? ' Needed: ' : ' Нужно: ') + picked.join(', ') + '.';
      }
      if (rush) { message += isEnglish ? ' Rather urgent.' : ' Хотелось бы срочно.'; }
      message += (isEnglish ? ' Estimate on the site: ' : ' Расчёт на сайте: ') +
                 formatRange(priceMin, priceMax) + ', ' + daysMin + '–' + daysMax +
                 (isEnglish ? ' days. Task:' : ' дней. Задача:');

      sendLink.href = 'https://t.me/DinoDafor?text=' + encodeURIComponent(message);
    };

    calcUpdate = update;
    calc.addEventListener('change', update);
    calc.addEventListener('submit', function (e) { e.preventDefault(); });
    update();
  }

  /* ---- 8. Бриф: ответы собираются в сообщение для Telegram ----
     Ничего никуда не отправляется: скрипт только строит текст ссылки. */

  var brief = document.querySelector('.brief');

  if (brief) {
    var briefLink = document.getElementById('brief-send');

    var names = ['business', 'pain', 'kind', 'tools', 'users', 'deadline', 'budget', 'extra'];
    var questions = names.map(function (name, i) { return [name, L.brief[i]]; });

    var collect = function () {
      var lines = [L.briefIntro, ''];

      questions.forEach(function (pair) {
        var name = pair[0];
        var field = brief.querySelector('[name="' + name + '"]');
        var value = '';

        if (field && field.tagName === 'TEXTAREA') {
          value = field.value.trim();
        } else {
          var checked = brief.querySelector('[name="' + name + '"]:checked');
          value = checked ? checked.value : '';
        }

        if (value) { lines.push(pair[1] + ': ' + value); }
      });

      briefLink.href = 'https://t.me/DinoDafor?text=' + encodeURIComponent(lines.join('\n'));
    };

    brief.addEventListener('input', collect);
    brief.addEventListener('change', collect);
    brief.addEventListener('submit', function (e) { e.preventDefault(); });
    collect();
  }

  /* ---- 9. Кнопки «скопировать» у контактов ---- */

  var copyButtons = document.querySelectorAll('.copy');

  Array.prototype.forEach.call(copyButtons, function (button) {
    var label = button.querySelector('.copy__label');
    var initial = label ? label.textContent : '';

    button.addEventListener('click', function () {
      var value = button.getAttribute('data-copy');
      if (!navigator.clipboard) { return; }

      navigator.clipboard.writeText(value).then(function () {
        button.classList.add('is-done');
        if (label) { label.textContent = L.copied; }

        setTimeout(function () {
          button.classList.remove('is-done');
          if (label) { label.textContent = initial; }
        }, 1800);
      }).catch(function () {});
    });
  });

  /* ---- 10. Яндекс.Метрика ----
     ВПИШИТЕ НОМЕР СЧЁТЧИКА в METRIKA_ID (только цифры, в кавычках).
     Пока строка пустая, никакая статистика не собирается и запросы не идут.
     Счётчик заводится на metrika.yandex.ru за пару минут.

     В самой Метрике заведите две цели типа «JavaScript-событие»
     с идентификаторами telegram_click и email_click — тогда в отчётах
     будет видно, сколько человек нажали «Написать» и на почту.

     Помните: со счётчиком сайт начинает собирать данные посетителей,
     поэтому нужна страница с политикой обработки персональных данных
     и ссылка на неё в подвале. */

  var METRIKA_ID = '';

  if (METRIKA_ID) {
    (function (m, e, t, r, i, k, a) {
      m[i] = m[i] || function () { (m[i].a = m[i].a || []).push(arguments); };
      m[i].l = 1 * new Date();
      for (var j = 0; j < e.scripts.length; j++) {
        if (e.scripts[j].src === r) { return; }
      }
      k = e.createElement(t); a = e.getElementsByTagName(t)[0];
      k.async = 1; k.src = r; a.parentNode.insertBefore(k, a);
    })(window, document, 'script', 'https://mc.yandex.ru/metrika/tag.js', 'ym');

    window.ym(METRIKA_ID, 'init', {
      clickmap: true,
      trackLinks: true,
      accurateTrackBounce: true,
      webvisor: true
    });

    document.addEventListener('click', function (e) {
      var a = e.target && e.target.closest ? e.target.closest('a') : null;
      if (!a || !a.href) { return; }

      if (a.href.indexOf('t.me/') !== -1) {
        window.ym(METRIKA_ID, 'reachGoal', 'telegram_click');
      } else if (a.href.indexOf('mailto:') === 0) {
        window.ym(METRIKA_ID, 'reachGoal', 'email_click');
      }
    });
  }

  /* ---- 11. Год в подвале ---- */

  var year = document.getElementById('year');
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
