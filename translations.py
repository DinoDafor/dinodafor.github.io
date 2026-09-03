# -*- coding: utf-8 -*-
"""Словарь для сборки английской версии.

Ключ — русская строка ровно так, как она стоит в HTML (лишние пробелы
схлопнуты). Значение — перевод. Добавили русский текст на страницу —
запустите build.py, он покажет, что осталось перевести.
"""

STRINGS = {
    # ---------- общее: шапка, подвал, cookie ----------
    'М': 'M',
    'Митин Михаил': 'Mikhail Mitin',
    'Митин Михаил · самозанятый': 'Mikhail Mitin · self-employed',
    'Написать': 'Message me',
    'Написать в Telegram': 'Message me on Telegram',
    'Валюта': 'Currency',
    'Перейти к содержимому': 'Skip to content',
    'Основная навигация': 'Main navigation',
    'Услуги': 'Services',
    'Расчёт': 'Estimate',
    'Кейсы': 'Case studies',
    'Проекты': 'Work',
    'Отзывы': 'Testimonials',
    'Вопросы': 'FAQ',
    'Обо мне': 'About',
    'Контакты': 'Contact',
    'Заметки': 'Notes',
    'На главную': 'Home',
    'Наверх ↑': 'Back to top ↑',
    'Политика конфиденциальности': 'Privacy policy',
    'Сайт использует файлы cookie сервиса веб-аналитики, чтобы понимать, какие разделы читают. Продолжая просмотр, вы соглашаетесь с этим — подробности в':
        'This site uses analytics cookies to see which sections people read. By continuing you agree to that — details in the',
    'политике обработки данных': 'privacy policy',
    'Сайт использует файлы cookie сервиса веб-аналитики, чтобы понимать, какие разделы читают. Продолжая просмотр, вы соглашаетесь с этим.':
        'This site uses analytics cookies to see which sections people read. By continuing you agree to that.',
    'Хорошо': 'Got it',

    # ---------- 404 ----------
    'Страница не найдена — Митин Михаил': 'Page not found — Mikhail Mitin',
    'Такой страницы на сайте нет. Вернитесь на главную или напишите в Telegram.':
        'There is no such page. Go back to the homepage or message me on Telegram.',
    'Ошибка 404': 'Error 404',
    'Такой страницы': 'This page',
    'здесь нет': 'does not exist',
    'Возможно, в адресе опечатка или страницу переименовали. С главной точно можно попасть куда нужно — а можно сразу написать мне.':
        'Perhaps the address has a typo, or the page was renamed. The homepage will get you where you need — or just message me.',

    # ---------- бриф ----------
    'Бриф на проект — Митин Михаил': 'Project brief — Mikhail Mitin',
    'Восемь вопросов о задаче: ответы собираются в сообщение и открываются в Telegram. Никаких форм и серверов.':
        'Eight questions about your task: the answers are collected into a message and opened in Telegram. No forms, no servers.',
    'Бриф': 'Brief',
    'Восемь вопросов — и я смогу назвать цену': 'Eight questions and I can quote a price',
    'Заполните, что знаете: пустые поля не страшны. В конце ответы соберутся в одно сообщение, которое откроется у вас в Telegram — останется нажать «отправить». Никуда, кроме вашего мессенджера, они не уходят: у сайта нет сервера, который мог бы их принять.':
        'Fill in what you know — blank fields are fine. At the end your answers are collected into a single message that opens in your Telegram; you only press “send”. They go nowhere else: this site has no server that could receive them.',
    '1. Чем занимается ваш бизнес': '1. What does your business do',
    'Например: сеть студий маникюра, три филиала в Казани':
        'For example: a chain of nail salons, three locations in Kazan',
    '2. Какой процесс хотите упростить': '2. Which process do you want to simplify',
    'Например: администратор вручную ведёт запись в переписке и путается в расписании':
        'For example: the receptionist books clients by hand in chat and keeps mixing up the schedule',
    '3. Что, по-вашему, нужно сделать': '3. What do you think needs to be built',
    'Чат-бот': 'Chatbot',
    'Сайт или лендинг': 'Website or landing page',
    'Интеграция сервисов': 'Service integration',
    'Автоматизация процесса': 'Process automation',
    'Пока не знаю, нужен совет': 'Not sure yet, I need advice',
    '4. Чем пользуетесь сейчас': '4. What do you use today',
    'Google Таблицы или Excel': 'Google Sheets or Excel',
    'Битрикс24': 'Bitrix24',
    '1С': '1C',
    'Ничего из этого': 'None of these',
    '5. Кто будет этим пользоваться': '5. Who will use it',
    'Клиенты': 'Customers',
    'Сотрудники': 'Employees',
    'И те и другие': 'Both',
    '6. Когда нужен результат': '6. When do you need it',
    'Чем скорее, тем лучше': 'As soon as possible',
    'В течение месяца': 'Within a month',
    'В течение квартала': 'Within a quarter',
    'Сроки не горят': 'No deadline pressure',
    '7. На какой бюджет рассчитываете': '7. What budget do you have in mind',
    'До 50 тысяч': 'Up to ₽50,000',
    '50–100 тысяч': '₽50,000–100,000',
    '100–200 тысяч': '₽100,000–200,000',
    'Больше 200 тысяч': 'Over ₽200,000',
    'Не определился, жду оценки': 'Undecided, waiting for your estimate',
    '8. Что ещё важно знать': '8. Anything else I should know',
    'Ссылки на примеры, ограничения, особенности — что угодно':
        'Links to examples, constraints, specifics — anything',
    'Отправить ответы в Telegram': 'Send answers to Telegram',
    'Сообщение соберётся автоматически. Перед отправкой его можно править.':
        'The message is assembled automatically. You can edit it before sending.',

    # ---------- кейс 1 ----------
    'Запись клиентов через Telegram-бота — кейс Митина Михаила':
        'Client booking through a Telegram bot — case study by Mikhail Mitin',
    'Как администратор перестал вести запись в переписке и вернул себе два часа каждый вечер.':
        'How a receptionist stopped booking clients in chat and got two hours back every evening.',
    'Студия маникюра, 3 филиала': 'Nail salon, 3 locations',
    'Запись клиентов через Telegram-бота': 'Client booking through a Telegram bot',
    'Сфера': 'Industry',
    'бьюти-услуги': 'beauty services',
    'Срок': 'Timeline',
    '9 дней': '9 days',
    'Бюджет': 'Budget',
    'Стек': 'Stack',
    'Заглушка скриншота: Запись клиентов через Telegram-бота':
        'Screenshot placeholder: client booking through a Telegram bot',
    'Задача': 'The problem',
    'Запись велась в переписке во «ВКонтакте», в Telegram и по телефону, а сводилась в общую таблицу вручную. Раз в неделю случалась двойная бронь: два мастера на одно время, недовольный клиент и извинения. Вечерняя сверка занимала у администратора полтора-два часа.':
        'Bookings came in through VK chat, Telegram and phone calls, then were copied into a shared spreadsheet by hand. Once a week there was a double booking: two specialists for the same slot, an unhappy client and apologies. Reconciling everything took the receptionist an hour and a half to two hours every evening.',
    'Что сделал': 'What I did',
    'Разобрал процесс: выписал все точки, где появляется запись, и нашёл, что 70% обращений — это четыре типовых вопроса.':
        'Mapped the process: listed every place a booking can appear and found that 70% of enquiries were four standard questions.',
    'Сделал бота: выбор филиала, мастера и свободного времени, перенос и отмена записи в два нажатия.':
        'Built the bot: choose a location, a specialist and an open slot; reschedule or cancel in two taps.',
    'Связал бота с общим календарём, чтобы занятые слоты исчезали сразу и у всех филиалов.':
        'Connected the bot to a shared calendar so booked slots disappear instantly across all locations.',
    'Добавил напоминание за три часа до визита и кнопку «не смогу прийти» — слот освобождается автоматически.':
        'Added a reminder three hours before the visit and a “can’t make it” button that frees the slot automatically.',
    'Собрал админ-раздел: список записей на день, выгрузка в таблицу, ручная блокировка времени.':
        'Built an admin area: the day’s bookings, export to a spreadsheet, manual blocking of time slots.',
    'Как это устроено': 'How it works',
    'Бот работает на сервере клиента, данные лежат в PostgreSQL, расписание синхронизируется с Google Календарём раз в минуту. При ошибке синхронизации бот пишет в служебный чат, а не молчит.':
        'The bot runs on the client’s server, data lives in PostgreSQL, and the schedule syncs with Google Calendar every minute. If a sync fails, the bot posts to an internal chat instead of staying silent.',
    'Результат': 'The result',
    'ручной работы администратора': 'less manual work for the receptionist',
    'неявок после напоминаний': 'fewer no-shows after reminders',
    'от старта до запуска': 'from start to launch',
    'Ожидала долгого внедрения, а бот заработал через полторы недели. Вечерняя сверка просто исчезла из рабочего дня.':
        'I expected a long rollout, but the bot was running in a week and a half. The evening reconciliation simply vanished from our day.',
    'АК': 'AK',
    'Анна Королёва, владелица сети студий': 'Anna Korolyova, owner of a salon chain',
    '← Все кейсы': '← All case studies',
    'Нужно похожее?': 'Need something similar?',
    'Расскажите, что нужно, — отвечу с оценкой срока и вилкой цены. Консультация бесплатная.':
        'Tell me what you need and I’ll reply with a timeline and a price range. The consultation is free.',

    # ---------- кейс 2 ----------
    'Синхронизация склада с маркетплейсом — кейс Митина Михаила':
        'Stock sync with a marketplace — case study by Mikhail Mitin',
    'Почему выгрузка остатков раз в сутки стоила клиенту рейтинга — и как это чинится за неделю.':
        'Why a once-a-day stock export was costing the client its rating — and how that is fixed in a week.',
    'Оптовая торговля': 'Wholesale',
    'Синхронизация склада с маркетплейсом': 'Stock sync with a marketplace',
    'оптовая торговля': 'wholesale',
    '11 дней': '11 days',
    'Заглушка скриншота: Синхронизация склада с маркетплейсом':
        'Screenshot placeholder: stock sync with a marketplace',
    'Остатки на площадку выгружались файлом раз в сутки. Товар, проданный офлайн утром, оставался в продаже до следующего дня: заказы приходилось отменять, рейтинг магазина падал, а менеджеры вели параллельную таблицу «что на самом деле есть».':
        'Stock levels were uploaded to the marketplace as a file once a day. An item sold offline in the morning stayed on sale until the next day: orders had to be cancelled, the shop’s rating dropped, and the sales team kept a parallel spreadsheet of “what we actually have”.',
    'Прослойка между учётной системой и площадкой: слушает изменения остатков и отправляет их пачками.':
        'A layer between the inventory system and the marketplace: it listens for stock changes and sends them in batches.',
    'Синхронизация каждые пять минут, а при крупных изменениях — сразу.':
        'Sync every five minutes, and immediately for large changes.',
    'Повтор запроса при ошибке с нарастающей паузой: временный сбой на стороне площадки больше не роняет обмен.':
        'Retries with an increasing back-off: a temporary failure on the marketplace side no longer breaks the exchange.',
    'Уведомления в Telegram-канал команды: что ушло, что не ушло и почему.':
        'Notifications to the team’s Telegram channel: what went through, what didn’t and why.',
    'Журнал операций, по которому видно историю каждого товара.':
        'An operation log that shows the history of every item.',
    'Сервис живёт в Docker на сервере клиента, состояние хранит в очереди, чтобы не терять изменения при перезапуске. Логи пишутся с ротацией, чтобы диск не заканчивался.':
        'The service runs in Docker on the client’s server and keeps its state in a queue so changes survive a restart. Logs are rotated so the disk never fills up.',
    '5 минут': '5 minutes',
    'задержка вместо суток': 'delay instead of a full day',
    'отмен заказов': 'fewer cancelled orders',
    'ручных выгрузок в день': 'manual uploads per day',
    'Интеграцию до этого пробовали делать дважды и оба раза бросали. Здесь получили рабочую синхронизацию и понятную инструкцию.':
        'We had tried this integration twice before and abandoned it both times. This time we got a working sync and a clear manual.',
    'МТ': 'MT',
    'Марина Т., руководитель отдела продаж': 'Marina T., head of sales',

    # ---------- кейс 3 ----------
    'Лендинг с калькулятором и заявками в CRM — кейс Митина Михаила':
        'Landing page with a calculator and leads in the CRM — case study by Mikhail Mitin',
    'Как убрать из разговора с клиентом первые пятнадцать минут выяснения очевидного.':
        'How to remove the first fifteen minutes of obvious questions from every sales call.',
    'Загородные дома': 'Country houses',
    'Лендинг с калькулятором и заявками в CRM': 'Landing page with a calculator and leads in the CRM',
    'строительство': 'construction',
    '7 дней': '7 days',
    'HTML, CSS, ванильный JS, amoCRM API': 'HTML, CSS, vanilla JS, amoCRM API',
    'Заглушка скриншота: Лендинг с калькулятором и заявками в CRM':
        'Screenshot placeholder: landing page with a calculator and CRM leads',
    'Реклама вела на страницу без структуры. Посетители не понимали порядок цен и уходили, а те, кто оставлял заявку, писали одно слово «интересует». Менеджер тратил первые минуты разговора на выяснение площади, этажности и бюджета.':
        'Ads led to a page with no structure. Visitors could not tell the ballpark price and left, and those who did enquire wrote a single word: “interested”. The sales manager spent the first minutes of every call asking about floor area, storeys and budget.',
    'Собрал структуру страницы вокруг одного вопроса клиента: сколько будет стоить дом под мои условия.':
        'Built the page around the one question a client has: how much will a house cost for my requirements.',
    'Калькулятор: площадь, этажность, материал, фундамент — считает вилку и показывает срок.':
        'A calculator: floor area, storeys, material, foundation — it shows a price range and a timeline.',
    'Короткий квиз из четырёх вопросов вместо формы с десятью полями.':
        'A short four-question quiz instead of a ten-field form.',
    'Заявка создаёт сделку в amoCRM с ответами клиента в карточке и уведомляет менеджера в Telegram.':
        'Each enquiry creates a deal in amoCRM with the client’s answers attached and pings the manager on Telegram.',
    'Аналитика с целями: видно, на каком шаге квиза людей теряем.':
        'Analytics with goals: it shows which quiz step loses people.',
    'Страница статическая, без CMS: грузится мгновенно и не требует обслуживания. Заявки уходят напрямую в CRM, ключ хранится на стороне сервера-посредника, а не в коде страницы.':
        'The page is static, with no CMS: it loads instantly and needs no maintenance. Enquiries go straight to the CRM, and the API key lives on a small proxy server rather than in the page code.',
    'конверсия в заявку': 'enquiry conversion rate',
    '2 минуты': '2 minutes',
    'среднее время ответа': 'average response time',
    'от макета до рекламы': 'from mock-up to live ads',
    'Менеджер стал звонить подготовленным. Раньше половина разговора уходила на вопросы, ответы на которые теперь есть сразу.':
        'Our manager now calls prepared. Half the conversation used to go on questions we already have answers to.',
    'ДС': 'DS',
    'Дмитрий Соколов, руководитель отдела продаж': 'Dmitry Sokolov, head of sales',

    # ---------- главная: голова и разметка ----------
    'Митин Михаил — боты, интеграции и сайты под ключ':
        'Mikhail Mitin — bots, integrations and websites, end to end',
    'Автоматизирую рутину малого бизнеса: чат-боты для Telegram и MAX, интеграции сервисов между собой, сайты и лендинги. Первый результат за 5–10 дней.':
        'I automate the routine work of small businesses: chatbots for Telegram and MAX, integrations between services, websites and landing pages. First result in 5–10 days.',
    'Автоматизирую рутину малого бизнеса: чат-боты для Telegram и MAX, интеграции сервисов между собой, сайты и лендинги.':
        'I automate the routine work of small businesses: chatbots for Telegram and MAX, integrations between services, websites and landing pages.',
    'Митин Михаил — автоматизация, боты и сайты': 'Mikhail Mitin — automation, bots and websites',
    'Разработчик, автоматизация бизнес-процессов': 'Developer, business process automation',
    'Разрабатываю чат-боты для Telegram и MAX, интеграции сервисов, сайты и лендинги для малого бизнеса.':
        'I build chatbots for Telegram and MAX, service integrations, websites and landing pages for small businesses.',
    'Разработка чат-ботов для Telegram': 'Telegram chatbot development',
    'Чат-боты для мессенджера MAX': 'Chatbots for the MAX messenger',
    'Интеграции сервисов через API': 'Service integrations over APIs',
    'Автоматизация бизнес-процессов': 'Business process automation',
    'Разработка сайтов и лендингов': 'Website and landing page development',
    'Страница с текстами, адаптивной вёрсткой, формами заявок и аналитикой под ключ.':
        'A page with copy, responsive markup, enquiry forms and analytics, delivered end to end.',
    'Разработка чат-ботов для Telegram и MAX': 'Chatbot development for Telegram and MAX',
    'Бот принимает заявки, отвечает на вопросы, ведёт запись и выгружает данные в CRM или таблицы.':
        'The bot takes enquiries, answers questions, handles booking and exports data to a CRM or spreadsheets.',
    'Замена ручных повторяющихся действий сценариями: отчёты, напоминания, контроль сроков.':
        'Repetitive manual steps replaced with scripts: reports, reminders, deadline tracking.',
    'Обмен данными между CRM, складом, платежами и сайтом: вебхуки, синхронизация, логирование.':
        'Data exchange between CRM, inventory, payments and the website: webhooks, sync, logging.',

    # ---------- FAQ ----------
    'Как проходит оплата?': 'How does payment work?',
    'Пополам: 50% предоплаты перед стартом и остаток при сдаче, после того как вы всё проверили. На больших проектах делим на этапы, чтобы вы платили за уже сделанное. Я самозанятый, чек присылаю сразу после платежа.':
        'In halves: 50% up front and the rest on delivery, once you have checked everything. Larger projects are split into stages so you pay for work already done. I am self-employed and send a receipt right after payment.',
    'Работаете по договору?': 'Do you work under a contract?',
    'Да, договор подряда с приложением, в котором прописан объём работ, сроки и стоимость. Работаю и с физлицами, и с компаниями. Если у вас свой шаблон договора — рассмотрю его.':
        'Yes — a service agreement with an annex covering scope, deadlines and price. I work with both individuals and companies. If you have your own contract template, I will review it.',
    'Может ли смета вырасти в процессе?': 'Can the estimate grow along the way?',
    'Названная сумма не меняется: всё, что попало в согласованный объём работ, входит в цену, даже если займёт больше времени, чем я рассчитывал. Отдельно оплачиваются только новые задачи, которых в списке не было, — и всегда с вашего письменного согласия.':
        'The quoted amount does not change: everything in the agreed scope is included, even if it takes me longer than planned. Only new tasks that were not on the list are billed separately — and always with your written approval.',
    'Кому принадлежит код и доступы?': 'Who owns the code and the accounts?',
    'Вам. Всё разворачивается на ваших аккаунтах и серверах, исходники передаю в ваш репозиторий, токены и пароли — вам в руки. Вы не привязаны ко мне: другой разработчик сможет продолжить работу.':
        'You do. Everything is deployed on your accounts and servers, the source goes into your repository, and tokens and passwords are handed to you. You are not tied to me: another developer can pick the work up.',
    'Что если результат не понравится?': 'What if I don’t like the result?',
    'До этого обычно не доходит: я показываю промежуточный результат каждые 2–3 дня, и вы правите курс по ходу, а не в день сдачи. Если после первого этапа станет ясно, что мы не сработались, — расходимся, я передаю сделанное и возвращаю неотработанную часть предоплаты.':
        'It rarely gets that far: I show progress every 2–3 days, so you steer as we go rather than on delivery day. If it becomes clear after the first stage that we are not a fit, we part ways — I hand over what is done and return the unearned part of the deposit.',
    'Что происходит после сдачи проекта?': 'What happens after the project is delivered?',
    '14 дней бесплатно правлю всё, что работает не так, как договаривались. Дальше — по вашему желанию: разовые доработки по часам или ежемесячная поддержка с приоритетным ответом. Бросать проект после оплаты мне невыгодно: клиенты возвращаются и рекомендуют.':
        'For 14 days I fix anything that does not work as agreed, free of charge. After that it is up to you: one-off changes billed hourly, or monthly support with priority response. Abandoning a project after payment makes no sense for me — clients come back and recommend me.',
    'Сколько проектов ведёте одновременно?': 'How many projects do you run at once?',
    'Два-три, не больше. Поэтому иногда прошу подождать неделю до старта — зато уже начатый проект не встаёт из-за того, что я занят у другого клиента.':
        'Two or three, no more. That is why I sometimes ask you to wait a week before we start — but a project already under way never stalls because I am busy with another client.',

    # ---------- первый экран ----------
    'Свободен для проектов с октября': 'Available for projects from October',
    'Автоматизирую рутину:': 'I automate the routine:',
    'боты, интеграции, сайты': 'bots, integrations, websites',
    'Убираю ручную работу из заявок, заказов и отчётов: заявки приходят в бота, данные сами едут в CRM и таблицы, а клиент видит понятный сайт. Первый рабочий результат — за 5–10 дней.':
        'I take the manual work out of enquiries, orders and reports: leads arrive in a bot, data travels to your CRM and spreadsheets on its own, and your client sees a clear website. First working result in 5–10 days.',
    'Смотреть кейсы': 'See case studies',
    'с 2018': 'since 2018',
    'в разработке и автоматизации': 'in development and automation',
    'запущенных проектов': 'projects launched',
    'Договор': 'Contract',
    'и фиксированная смета': 'and a fixed estimate',
    'Пример: бот записи в студию': 'Example: a salon booking bot',
    'Бот студии': 'Salon bot',
    'отвечает сразу': 'replies instantly',
    'Здравствуйте! Хочу записаться на маникюр': 'Hi! I’d like to book a manicure',
    'Привет! В какой филиал удобно?': 'Hi! Which location works for you?',
    'На Ленина': 'Lenina street',
    'На Мира': 'Mira avenue',
    'Завтра свободно: 11:00, 14:30, 18:00': 'Tomorrow is open at 11:00, 14:30, 18:00',
    'Записала вас на 14:30, мастер Ольга. Напомню за 3 часа':
        'Booked you for 14:30 with Olga. I’ll remind you 3 hours before',
    'Так это выглядит для клиента. Заявка сразу уходит в таблицу и в CRM.':
        'This is what the client sees. The booking goes straight into a spreadsheet and the CRM.',

    # ---------- логотипы ----------
    'С кем работал': 'Clients I’ve worked with',
    'Место под логотип клиента': 'Placeholder for a client logo',

    # ---------- услуги ----------
    'Что я делаю и сколько это стоит': 'What I do and what it costs',
    'Цены — за проект под ключ, без почасовки. Точная смета появляется после короткого созвона и списка задач.':
        'Prices are per project, end to end, not hourly. The exact estimate follows a short call and a list of tasks.',
    'Сайты и лендинги': 'Websites and landing pages',
    'Страница, которая объясняет продукт и собирает заявки, а не просто «есть в интернете».':
        'A page that explains your product and collects enquiries, rather than merely existing online.',
    'Структура и тексты по вашему продукту': 'Structure and copy based on your product',
    'Вёрстка от 360 до 1440 px, скорость и SEO-база': 'Layout from 360 to 1440 px, speed and SEO basics',
    'Формы с отправкой в Telegram или почту': 'Forms delivered to Telegram or email',
    'Аналитика, домен, хостинг, передача доступов': 'Analytics, domain, hosting, handover of accounts',
    '5–10 дней': '5–10 days',
    'Цена': 'Price',
    'от': 'from',
    'от 45 000 ₽': 'from ₽45,000',
    'Чат-боты для Telegram и MAX': 'Chatbots for Telegram and MAX',
    'Бот принимает заявки, отвечает на частые вопросы и снимает нагрузку с менеджера.':
        'The bot takes enquiries, answers common questions and takes load off your manager.',
    'Сценарий диалога, меню и кнопки': 'Dialogue script, menus and buttons',
    'Заявки, запись, оплата, рассылки по базе': 'Enquiries, booking, payments, broadcasts to your list',
    'Админ-раздел: заявки, статусы, уведомления': 'Admin area: enquiries, statuses, notifications',
    'Выгрузка данных в Google Sheets или CRM': 'Data export to Google Sheets or a CRM',
    '7–14 дней': '7–14 days',
    'от 60 000 ₽': 'from ₽60,000',
    'Автоматизация процессов': 'Process automation',
    'Нахожу повторяющиеся действия сотрудников и заменяю их сценарием, который работает сам.':
        'I find repetitive actions your staff perform and replace them with a script that runs itself.',
    'Разбор процесса и карта «где теряется время»': 'Process review and a map of where time is lost',
    'Скрипты и сценарии вместо ручного копирования': 'Scripts instead of manual copying',
    'Автоотчёты, напоминания, контроль сроков': 'Automatic reports, reminders, deadline tracking',
    'Инструкция для команды и обучение': 'A manual for your team and training',
    '3–14 дней': '3–14 days',
    'от 30 000 ₽': 'from ₽30,000',
    'Интеграции и API': 'Integrations and APIs',
    'Связываю сервисы, которые «не дружат»: сайт, CRM, склад, платежи, мессенджеры.':
        'I connect services that don’t talk to each other: website, CRM, inventory, payments, messengers.',
    'Обмен данными между CRM, таблицами и сайтом': 'Data exchange between CRM, spreadsheets and the site',
    'Вебхуки, очереди, регулярная синхронизация': 'Webhooks, queues, scheduled synchronisation',
    'Обработка ошибок, повторы, логи и алерты': 'Error handling, retries, logs and alerts',
    'Документация по интеграции для вашей команды': 'Integration documentation for your team',
    '4–12 дней': '4–12 days',
    'от 40 000 ₽': 'from ₽40,000',

    # ---------- калькулятор ----------
    'Прикиньте бюджет за минуту': 'Estimate your budget in a minute',
    'Соберите проект из блоков — покажу вилку и срок. Это ориентир, а не смета: точную цену назову после короткого разговора, и она не вырастет по ходу работы.':
        'Assemble your project from blocks and I’ll show a range and a timeline. It is a guide, not a quote: the exact price comes after a short call, and it does not grow later.',
    'Что нужно сделать': 'What needs building',
    'Чат-бот для Telegram или MAX': 'Chatbot for Telegram or MAX',
    'Telegram или MAX': 'Telegram or MAX',
    'Сайт': 'Website',
    'лендинг или визитка': 'landing page or a small site',
    'Интеграция': 'Integration',
    'связать сервисы между собой': 'connect services to each other',
    'Автоматизация': 'Automation',
    'убрать ручную рутину': 'remove manual routine',
    'Что добавить': 'What to add',
    'приём оплаты': 'payments',
    'Приём оплаты': 'Payments',
    'карты, СБП, чеки': 'cards, instant transfers, receipts',
    'выгрузка в CRM или таблицы': 'export to a CRM or spreadsheets',
    'Выгрузка в CRM или таблицы': 'Export to a CRM or spreadsheets',
    'заявки не теряются': 'no enquiry gets lost',
    'админ-панель с отчётами': 'admin panel with reports',
    'Админ-панель с отчётами': 'Admin panel with reports',
    'видеть заявки и статистику': 'see enquiries and statistics',
    'ответы на частые вопросы': 'answers to common questions',
    'Ответы на частые вопросы': 'Answers to common questions',
    'бот разгружает менеджера': 'the bot unloads your manager',
    'тексты и подбор изображений': 'copy and images',
    'Тексты и изображения': 'Copy and images',
    'не придётся писать самому': 'you won’t have to write it yourself',
    'индивидуальный дизайн': 'custom design',
    'Индивидуальный дизайн': 'Custom design',
    'вместо типовой структуры': 'instead of a standard layout',
    'перенос данных из старой системы': 'data migration from the old system',
    'Перенос данных': 'Data migration',
    'из старой системы или таблиц': 'from an old system or spreadsheets',
    'поддержка 3 месяца': '3 months of support',
    'Поддержка 3 месяца': '3 months of support',
    'правки и ответы вне очереди': 'priority fixes and answers',
    'Нужно срочно': 'I need it urgently',
    'беру в работу вне очереди, срок короче примерно на треть':
        'I take it on out of turn; the timeline shrinks by roughly a third',
    'Ориентировочно': 'Ballpark',
    '7–14 рабочих дней': '7–14 working days',
    'Отправить расчёт в Telegram': 'Send the estimate to Telegram',
    'Расчёт подставится в сообщение — останется дописать пару слов о задаче.':
        'The estimate is inserted into the message — just add a couple of words about your task.',
    'Цены в рублях; в другой валюте — пересчёт по курсу для ориентира.':
        'Prices are in roubles; other currencies are converted for reference.',

    # ---------- гарантии и поддержка ----------
    'Гарантии': 'Guarantees',
    'Что вы получаете в любом случае': 'What you get in any case',
    'Подряд с объёмом работ, сроками и стоимостью в приложении. Закрывающие документы предоставляю.':
        'A service agreement with scope, deadlines and price in an annex. I provide closing documents.',
    'Фиксированная смета': 'Fixed estimate',
    'Названная сумма не растёт по ходу работы. Новые задачи — только с вашего письменного согласия.':
        'The quoted amount does not grow during the work. New tasks only with your written approval.',
    '14 дней правок': '14 days of fixes',
    'После сдачи бесплатно правлю всё, что работает не так, как договаривались. Без споров о формулировках.':
        'After delivery I fix anything that does not work as agreed, free of charge. No arguing over wording.',
    'Код и доступы ваши': 'The code and accounts are yours',
    'Исходники в вашем репозитории, всё развёрнуто на ваших аккаунтах. Продолжить работу сможет любой разработчик.':
        'Source in your repository, everything deployed on your accounts. Any developer can continue the work.',
    'Поддержка': 'Support',
    'Что дальше, после запуска': 'What happens after launch',
    'Первые 14 дней правок входят в проект. Дальше — как удобнее вам: можно вообще без сопровождения, код и доступы у вас, и продолжить сможет любой разработчик.':
        'The first 14 days of fixes are included. After that it is up to you: you can go without support entirely — the code and accounts are yours, and any developer can continue.',
    'Без подписки': 'Pay as you go',
    'от 3 500 ₽': 'from ₽3,500',
    'за час': 'per hour',
    'Разовые доработки по мере надобности. Беру в работу в порядке очереди, обычно в течение недели.':
        'One-off changes whenever you need them. Handled in order of arrival, usually within a week.',
    'Оплата по факту, минимум 2 часа': 'Paid after the fact, 2-hour minimum',
    'Оценка задачи до старта': 'Every task estimated before it starts',
    'Чаще всего берут': 'Most popular',
    'Базовая': 'Basic',
    'от 12 000 ₽': 'from ₽12,000',
    'в месяц': 'per month',
    'Мелкие правки и присмотр за тем, чтобы всё работало. Подходит, если бот или интеграция уже в деле.':
        'Small fixes and keeping an eye on things. A good fit once your bot or integration is live.',
    'До 4 часов работ в месяц': 'Up to 4 hours of work per month',
    'Ответ в течение рабочего дня': 'Reply within a business day',
    'Слежу за ошибками и уведомляю сам': 'I watch for errors and tell you first',
    'Приоритетная': 'Priority',
    'Когда простой стоит денег: заявки идут через бота, а склад синхронизируется каждые пять минут.':
        'For when downtime costs money: enquiries come through the bot and stock syncs every five minutes.',
    'До 10 часов работ в месяц': 'Up to 10 hours of work per month',
    'Ответ в течение 2 часов в будни': 'Reply within 2 hours on business days',
    'Срочные поломки — вне очереди': 'Urgent breakages jump the queue',

    # ---------- кейсы на главной ----------
    'Задача → решение → результат': 'Problem → solution → result',
    'Три примера того, как выглядит работа. Тексты и цифры замените на свои проекты.':
        'Three examples of what the work looks like. Replace the text and numbers with your own projects.',
    'Администратор вручную вёл запись в переписке и таблице: терялись клиенты, случались двойные брони, вечером уходило до двух часов на сверку.':
        'The receptionist booked clients by hand in chat and a spreadsheet: clients slipped through, double bookings happened, and evenings cost up to two hours of reconciliation.',
    'Решение': 'Solution',
    'Бот с выбором филиала, мастера и свободного времени, автонапоминанием за 3 часа и переносом записи в два клика. Расписание синхронизируется с календарём, все записи падают в общую таблицу.':
        'A bot for choosing a location, a specialist and an open slot, with an automatic 3-hour reminder and rescheduling in two clicks. The schedule syncs with a calendar and every booking lands in a shared spreadsheet.',
    'Запись работает круглосуточно и без администратора, неявки заметно сократились, ручная сверка исчезла как задача.':
        'Booking now runs around the clock without a receptionist, no-shows dropped noticeably, and manual reconciliation disappeared as a task.',
    'Разобрать кейс подробно →': 'Read the full case study →',
    'Остатки обновляли выгрузкой раз в сутки. Товары, проданные офлайн, оставались в продаже онлайн — заказы приходилось отменять, рейтинг падал.':
        'Stock was updated by a daily export. Items sold offline stayed on sale online — orders had to be cancelled and the rating fell.',
    'Сервис-прослойка: слушает изменения в учётной системе, каждые 5 минут отправляет остатки и цены в личный кабинет площадки, при ошибке повторяет запрос и пишет в Telegram-канал команды.':
        'A middle layer: it watches the inventory system, pushes stock and prices to the marketplace every 5 minutes, retries on failure and reports to the team’s Telegram channel.',
    'Отмены из-за отсутствия товара практически прекратились, менеджеры перестали вести параллельные таблицы.':
        'Cancellations due to missing stock have all but stopped, and the team no longer keeps parallel spreadsheets.',
    '5 мин': '5 min',
    'Node.js · REST API · вебхуки · Docker': 'Node.js · REST API · webhooks · Docker',
    'Лендинг с квизом и заявками в CRM': 'Landing page with a quiz and CRM leads',
    'Реклама вела на страницу без структуры: посетители не понимали цену и уходили, заявки приходили на почту и терялись.':
        'Ads led to a page with no structure: visitors could not tell the price and left, and enquiries arrived by email and got lost.',
    'Одностраничник с калькулятором стоимости и коротким квизом из четырёх вопросов. Заявка сразу создаёт сделку в CRM с ответами клиента и уведомляет менеджера в Telegram.':
        'A one-pager with a price calculator and a short four-question quiz. Each enquiry creates a CRM deal with the client’s answers and pings the manager on Telegram.',
    'Менеджер звонит подготовленным, а не выясняет базовые вопросы. Конверсия в заявку выросла, ни одно обращение не теряется.':
        'The manager calls prepared instead of asking the basics. Enquiry conversion went up and nothing gets lost.',
    '2 мин': '2 min',
    'HTML · CSS · ванильный JS · amoCRM API': 'HTML · CSS · vanilla JS · amoCRM API',

    # ---------- проекты ----------
    'Что я уже сделал': 'What I have built',
    'Небольшая витрина работ: бот, интеграция или сайт — и что конкретно он делает. Подробности по любому проекту расскажу в переписке.':
        'A short showcase: a bot, an integration or a website — and exactly what it does. I’ll tell you more about any of them in chat.',
    'Заглушка скриншота проекта: бот записи клиентов':
        'Project screenshot placeholder: client booking bot',
    'Бот записи для сети студий': 'Booking bot for a salon chain',
    'Клиент выбирает филиал, мастера и свободное время прямо в чате, бот напоминает о визите и переносит запись.':
        'The client picks a location, a specialist and a free slot right in chat; the bot reminds them and reschedules.',
    'Обсудить похожий →': 'Discuss something similar →',
    'Заглушка скриншота проекта: синхронизация склада с маркетплейсом':
        'Project screenshot placeholder: stock sync with a marketplace',
    'Остатки и цены уезжают из учётной системы на площадку каждые пять минут, ошибки повторяются и падают в Telegram команде.':
        'Stock and prices leave the inventory system for the marketplace every five minutes; failures are retried and reported to the team on Telegram.',
    'Заглушка скриншота проекта: лендинг с калькулятором стоимости':
        'Project screenshot placeholder: landing page with a price calculator',
    'Лендинг с калькулятором стоимости': 'Landing page with a price calculator',
    'Посетитель считает цену дома по параметрам и оставляет заявку, которая сразу создаёт сделку в CRM с его ответами.':
        'A visitor prices a house by parameters and leaves an enquiry that instantly creates a CRM deal with their answers.',
    'ванильный JS': 'vanilla JS',
    'Заглушка скриншота проекта: бот поддержки в мессенджере MAX':
        'Project screenshot placeholder: support bot in the MAX messenger',
    'Бот поддержки в MAX': 'Support bot in MAX',
    'Отвечает на частые вопросы сервисного центра, принимает заявки на ремонт и показывает статус по номеру заказа.':
        'It answers a service centre’s common questions, takes repair requests and shows the status by order number.',
    'Заглушка скриншота проекта: автоматические отчёты из CRM':
        'Project screenshot placeholder: automated CRM reports',
    'Отчёты из CRM по расписанию': 'Scheduled CRM reports',
    'Каждое утро руководитель получает в Telegram сводку по сделкам, звонкам и просроченным задачам вместо ручной выгрузки.':
        'Every morning the manager gets a Telegram digest of deals, calls and overdue tasks instead of exporting by hand.',
    'Заглушка скриншота проекта: каталог товаров с выгрузкой в 1С':
        'Project screenshot placeholder: product catalogue with 1C export',
    'Каталог с выгрузкой в 1С': 'Catalogue with 1C export',
    'Витрина с фильтрами и корзиной: заказ уходит в 1С, менеджер видит его в привычном интерфейсе без копирования вручную.':
        'A storefront with filters and a cart: the order goes into 1C and the manager sees it in the familiar interface without copying anything.',
    '1С: обмен': '1C exchange',

    # ---------- процесс ----------
    'Процесс': 'Process',
    'Как я работаю': 'How I work',
    'Четыре шага от первого сообщения до сданного проекта. Без пропавших недель и «ещё пару дней».':
        'Four steps from your first message to a delivered project. No vanished weeks and no “just a couple more days”.',
    'Заявка и разбор': 'Enquiry and review',
    'Созвон на 30 минут: что за процесс, где болит, что считаем успехом. Если задача не моя — честно скажу сразу. Можно начать с':
        'A 30-minute call: what the process is, where it hurts, what counts as success. If the task is not for me, I say so straight away. You can start with the',
    'брифа': 'brief',
    'Смета и план': 'Estimate and plan',
    'Присылаю объём работ, сроки по этапам и фиксированную цену. После согласования — договор и предоплата 50%.':
        'I send the scope, stage-by-stage deadlines and a fixed price. Once agreed: contract and a 50% deposit.',
    'Разработка и демо': 'Development and demos',
    'Показываю промежуточный результат раз в 2–3 дня. Вы правите на ходу, а не в последний день перед сдачей.':
        'I show progress every 2–3 days. You steer as we go, not on the last day before delivery.',
    'Запуск и поддержка': 'Launch and support',
    'Перенос на ваши серверы и аккаунты, инструкция и обучение команды, 14 дней бесплатных правок после сдачи.':
        'Moving everything to your servers and accounts, a manual and training for your team, 14 days of free fixes after delivery.',

    # ---------- сравнение ----------
    'Сравнение': 'Comparison',
    'Один разработчик, студия или сотрудник в штат': 'One developer, an agency or an in-house hire',
    'Честно о том, где я выигрываю, а где нет. Если по таблице выходит, что вам нужна студия, — так и скажу на созвоне.':
        'An honest look at where I win and where I don’t. If the table says you need an agency, I’ll say so on the call.',
    'Сравнение работы с фрилансером, студией и штатным разработчиком':
        'Comparison of working with a freelancer, an agency and an in-house developer',
    'Я, один': 'Me, solo',
    'Студия': 'Agency',
    'Сотрудник в штат': 'In-house hire',
    'Стоимость бота с интеграцией': 'Cost of a bot with an integration',
    'от 250 000 ₽': 'from ₽250,000',
    'от 150 000 ₽': 'from ₽150,000',
    'Старт работ': 'Time to start',
    '2–5 дней': '2–5 days',
    '2–4 недели': '2–4 weeks',
    '1–2 месяца на поиск': '1–2 months to hire',
    'Кто пишет код': 'Who writes the code',
    'Я, с кем вы и говорите': 'Me — the person you are talking to',
    'Обычно джуниор, а общаетесь с менеджером': 'Usually a junior; you talk to an account manager',
    'Ваш сотрудник': 'Your employee',
    'Если задача выросла втрое': 'If the task triples in size',
    'Не потяну один, честно скажу заранее': 'I can’t do it alone — I’ll tell you in advance',
    'Подключат команду': 'They add more people',
    'Наймёте ещё людей': 'You hire more people',
    'Что через полгода': 'Six months later',
    'Отвечаю на письма, код у вас': 'I answer emails; the code is yours',
    'Поддержка по договору': 'Support under contract',
    'Всё в вашей команде': 'Everything stays in your team',
    'Коротко: я дешевле и быстрее на задачах, которые тянет один человек за 2–6 недель. На проекте с командой из пяти человек и годовым горизонтом выгоднее студия — это нормально.':
        'In short: I am cheaper and faster on tasks one person can carry in 2–6 weeks. For a project needing a team of five over a year, an agency is the better deal — and that is fine.',

    # ---------- обо мне ----------
    'Коротко о том, с кем вы будете работать': 'A few words about who you’ll be working with',
    'Меня зовут Михаил, я разработчик на фрилансе и с 2018 года делаю то, что экономит людям часы: боты, интеграции и сайты для небольших компаний. Обычно ко мне приходят, когда бизнес уже работает, но держится на переписках и десятке таблиц. Я разбираюсь в процессе, предлагаю самое простое решение из работающих и довожу его до продакшена — без лишних сервисов и подписок, которые потом непонятно кто оплачивает. Работаю один, поэтому веду 2–3 проекта одновременно и отвечаю в течение рабочего дня.':
        'My name is Mikhail. I am a freelance developer and since 2018 I have been building things that save people hours: bots, integrations and websites for small companies. People usually come to me when the business already works but runs on chat threads and a dozen spreadsheets. I dig into the process, propose the simplest solution that works and take it to production — without extra services and subscriptions nobody remembers paying for. I work alone, so I run 2–3 projects at a time and reply within the business day.',
    'Пишу понятный код и передаю его вместе с доступами — вас никто не держит на привязи.':
        'I write readable code and hand it over with the accounts — nobody keeps you on a leash.',
    'Согласовываю смету до старта: итог не отличается от названной цены.':
        'The estimate is agreed before we start: the final bill matches the quoted price.',
    'Работаю по договору, самозанятый — закрывающие документы предоставляю.':
        'I work under a contract as a self-employed professional and provide closing documents.',
    'Заглушка вместо фотографии Михаила Митина': 'Placeholder for a photo of Mikhail Mitin',
    'Технологии': 'Technologies',
    'REST / вебхуки': 'REST / webhooks',

    # ---------- отзывы ----------
    'Что говорят клиенты': 'What clients say',
    'Короткие отзывы тех, с кем я работал. Контакты для рекомендаций дам по запросу.':
        'Short testimonials from people I have worked with. References available on request.',
    'Ожидала долгого внедрения, а бот заработал через полторы недели. Администратор перестал вести запись в переписке, и вечерняя сверка просто исчезла из рабочего дня.':
        'I expected a long rollout, but the bot was running in a week and a half. Our receptionist stopped booking in chat and the evening reconciliation simply vanished from the day.',
    'Анна Королёва': 'Anna Korolyova',
    'владелица сети студий, Москва': 'owner of a salon chain, Moscow',
    'Главное — объяснял решения человеческим языком и не тянул с ответами. Смета в итоге совпала с названной на старте, без внезапных доработок за отдельные деньги.':
        'Most importantly, he explained decisions in plain language and answered quickly. The final bill matched the initial estimate, with no surprise extras.',
    'Дмитрий Соколов': 'Dmitry Sokolov',
    'руководитель отдела продаж': 'head of sales',
    'Интеграцию со складом до этого пробовали делать дважды и оба раза бросали. Здесь получили рабочую синхронизацию и понятную инструкцию, разобрался даже наш бухгалтер.':
        'We had tried the stock integration twice before and abandoned it both times. This time we got a working sync and a clear manual — even our accountant figured it out.',
    'Марина Т.': 'Marina T.',
    'оптовая торговля, Казань': 'wholesale, Kazan',
    'Голосовые отзывы': 'Voice testimonials',
    'Иногда клиенту проще наговорить пару минут, чем писать текст. Нажмите на плей.':
        'Sometimes it is easier for a client to talk for two minutes than to write. Press play.',
    'ИВ': 'IV',
    'Игорь В.': 'Igor V.',
    'сервисный центр': 'service centre',
    'Ваш браузер не умеет проигрывать аудио.': 'Your browser cannot play audio.',
    'Скачать запись': 'Download the recording',
    '0:00 · заглушка, замените на свой файл': '0:00 · placeholder, replace with your own file',
    'ЕЛ': 'EL',
    'Елена Л.': 'Elena L.',
    'интернет-магазин': 'online shop',

    # ---------- FAQ и заметки на главной ----------
    'Что обычно спрашивают до старта': 'What people usually ask before we start',
    'Если вашего вопроса здесь нет — напишите, отвечу без общих слов.':
        'If your question isn’t here, message me — I’ll answer without vague generalities.',
    'Пишу о том, что спрашивают чаще всего': 'I write about what people ask most often',
    'Разбираю вопросы, которые всплывают в переписке с каждым вторым клиентом.':
        'I unpack the questions that come up with every other client.',
    'Деньги': 'Money',
    'Сколько стоит Telegram-бот и из чего складывается цена':
        'What a Telegram bot costs and what makes up the price',
    'Почему один бот стоит 40 тысяч, а похожий на вид — 200, и на чём точно не стоит экономить.':
        'Why one bot costs ₽40,000 and a similar-looking one ₽200,000 — and what you should never cut.',
    'Читать →': 'Read →',
    'Процессы': 'Processes',
    'Что автоматизировать первым, если бюджет один': 'What to automate first when you can afford one thing',
    'Простой способ найти процесс, который окупит автоматизацию быстрее остальных.':
        'A simple way to find the process that pays automation back fastest.',
    'Мессенджеры': 'Messengers',
    'MAX или Telegram: где делать бота для бизнеса': 'MAX or Telegram: where to build a business bot',
    'Чем отличаются платформы с точки зрения заказчика и почему часто нужны обе.':
        'How the platforms differ from the client’s point of view and why you often need both.',
    'Все заметки →': 'All notes →',

    # ---------- контакты ----------
    'Расскажите задачу — отвечу с оценкой': 'Tell me about your task — I’ll reply with an estimate',
    'Напишите пару предложений о процессе, который хотите упростить. В ответ пришлю вопросы, примерный срок и вилку цены. Консультация бесплатная и ни к чему не обязывает.':
        'Write a couple of sentences about the process you want to simplify. I’ll come back with questions, a rough timeline and a price range. The consultation is free and commits you to nothing.',
    'Скопировать ник': 'Copy handle',
    'Почта': 'Email',
    'Скопировать почту': 'Copy email',
    'Скопировать ссылку': 'Copy link',
    'Работаю по московскому времени, отвечаю в будни с 10:00 до 20:00. Не любите переписку —':
        'I work on Moscow time and reply on weekdays from 10:00 to 20:00 (UTC+3). If you would rather not chat,',
    'заполните короткий бриф': 'fill in the short brief',
    ', и я отвечу сразу с оценкой.': ' and I’ll come straight back with an estimate.',

    # ---------- политика ----------
    'Политика обработки персональных данных — Митин Михаил':
        'Personal data processing policy — Mikhail Mitin',
    'Как сайт dinodafor.github.io обрабатывает персональные данные посетителей: какие данные собираются, зачем, кому передаются и как отозвать согласие.':
        'How dinodafor.github.io processes visitors’ personal data: what is collected, why, who receives it and how to withdraw consent.',
    'Политика обработки персональных данных': 'Personal data processing policy',
    'Какие данные собирает сайт, зачем, кому передаются и как отозвать согласие.':
        'What the site collects, why, who receives it and how to withdraw consent.',
    'Правовая информация': 'Legal',
    'Редакция от 3 сентября 2026 года': 'Version of 3 September 2026',
    '1. Общие положения': '1. General',
    'Настоящая Политика описывает, какие персональные данные собираются на сайте':
        'This Policy describes what personal data is collected on the website',
    '(далее — Сайт), с какой целью они обрабатываются, кому передаются и какие права есть у посетителя.':
        '(the “Site”), why it is processed, who receives it and what rights a visitor has.',
    'Оператором персональных данных является Митин Михаил Владиславович, применяющий специальный налоговый режим «Налог на профессиональный доход», ИНН':
        'The data operator is Mikhail Vladislavovich Mitin, registered under the Russian “professional income tax” regime, taxpayer number',
    '[укажите ИНН]': '[add your taxpayer number]',
    '(далее — Оператор).': '(the “Operator”).',
    'Политика подготовлена в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных». Продолжая пользоваться Сайтом, посетитель соглашается с условиями настоящей Политики. Если вы не согласны — покиньте Сайт или отключите файлы cookie в настройках браузера.':
        'This Policy follows Russian Federal Law No. 152-FZ of 27 July 2006 “On Personal Data”. By continuing to use the Site you accept this Policy. If you do not agree, please leave the Site or disable cookies in your browser settings.',
    '2. Какие данные обрабатываются': '2. What data is processed',
    'На Сайте нет форм обратной связи, регистрации и личного кабинета. Посетитель не вводит на Сайте никаких данных о себе.':
        'The Site has no contact forms, registration or user accounts. A visitor enters no personal data on the Site.',
    'Обрабатываются только две категории сведений:': 'Only two categories of information are processed:',
    'Обезличенные данные о посещении': 'Anonymised visit data',
    ', которые собирает сервис веб-аналитики: IP-адрес, сведения об устройстве и браузере, операционная система, разрешение экрана, язык, источник перехода, посещённые страницы, время и глубина просмотра, клики и прокрутка, идентификаторы файлов cookie.':
        ' collected by the analytics service: IP address, device and browser details, operating system, screen resolution, language, referrer, pages visited, time and depth of browsing, clicks and scrolling, cookie identifiers.',
    'Данные, которые вы сообщаете сами': 'Data you provide yourself',
    ', если решаете написать Оператору в Telegram или на электронную почту: имя или никнейм, контактные данные и содержание вашего сообщения. Эти данные вы передаёте по своей инициативе и в объёме, который выбираете сами.':
        ' if you choose to message the Operator on Telegram or by email: your name or handle, contact details and the content of your message. You share this on your own initiative and in the amount you choose.',
    'Оператор не собирает специальные и биометрические категории персональных данных и не обрабатывает данные несовершеннолетних осознанно.':
        'The Operator does not collect special or biometric categories of personal data and does not knowingly process data of minors.',
    '3. Веб-аналитика': '3. Web analytics',
    'На Сайте используется сервис Яндекс Метрика, принадлежащий ООО «ЯНДЕКС» (Россия, 119021, Москва, ул. Льва Толстого, д. 16). Сервис собирает обезличенные данные о посещениях, включая запись действий посетителя на странице (Вебвизор), и передаёт их Оператору в виде сводных отчётов.':
        'The Site uses Yandex Metrica, operated by Yandex LLC (16 Lva Tolstogo St., Moscow, 119021, Russia). The service collects anonymised visit data, including session recordings (Webvisor), and provides the Operator with aggregated reports.',
    'Условия обработки данных сервисом изложены в': 'The service’s terms are set out in the',
    'Политике конфиденциальности Яндекса': 'Yandex Privacy Policy',
    '. Отказаться от сбора данных Метрикой можно с помощью': '. You can opt out of Metrica tracking with a',
    'специального дополнения для браузера': 'dedicated browser add-on',
    '4. Цели обработки': '4. Purposes of processing',
    'оценка удобства Сайта и его улучшение: какие разделы читают, где посетители уходят;':
        'assessing and improving the Site: which sections people read and where they leave;',
    'оценка эффективности размещения ссылок на Сайт;': 'measuring how well links to the Site perform;',
    'ответ на обращение, если вы написали Оператору, и последующее обсуждение возможного сотрудничества.':
        'replying to your message and discussing possible cooperation.',
    'Данные не используются для принятия решений на основании исключительно автоматизированной обработки, порождающих юридические последствия для посетителя.':
        'The data is not used for solely automated decisions producing legal effects for the visitor.',
    '5. Правовые основания': '5. Legal grounds',
    'Обработка обезличенных данных о посещении осуществляется на основании согласия посетителя, выражаемого продолжением использования Сайта с включёнными файлами cookie. Обработка данных из вашего обращения — на основании вашего согласия, выраженного самим фактом отправки сообщения, и в целях исполнения договора или подготовки к его заключению.':
        'Anonymised visit data is processed on the basis of the visitor’s consent, expressed by continuing to use the Site with cookies enabled. Data from your message is processed on the basis of your consent, expressed by sending it, and in order to perform or prepare a contract.',
    '6. Файлы cookie': '6. Cookies',
    'Cookie — небольшие текстовые файлы, которые сохраняются в вашем браузере. На Сайте они используются только сервисом веб-аналитики для того, чтобы отличать новых посетителей от вернувшихся. Собственных cookie Сайт не устанавливает и рекламных сетей не подключает.':
        'Cookies are small text files stored in your browser. On this Site they are used only by the analytics service to tell new visitors from returning ones. The Site sets no cookies of its own and uses no ad networks.',
    'Вы можете запретить cookie в настройках браузера или удалить уже сохранённые. Сайт продолжит работать: ни один раздел не требует cookie.':
        'You can block cookies in your browser settings or delete the ones already stored. The Site will keep working: no section requires cookies.',
    '7. Передача данных третьим лицам': '7. Sharing with third parties',
    'Оператор не продаёт и не передаёт персональные данные третьим лицам, за исключением:':
        'The Operator does not sell or share personal data with third parties, except:',
    'ООО «ЯНДЕКС» — как сервису веб-аналитики, в объёме, описанном в разделе 3;':
        'Yandex LLC, as the analytics provider, to the extent described in section 3;',
    'компании GitHub, Inc., на инфраструктуре которой размещён Сайт (GitHub Pages) и которая обрабатывает технические данные о запросах к серверу;':
        'GitHub, Inc., whose infrastructure hosts the Site (GitHub Pages) and which processes technical data about server requests;',
    'случаев, когда передача требуется по закону — по мотивированному запросу уполномоченных государственных органов.':
        'cases where disclosure is required by law, upon a substantiated request from authorised state bodies.',
    'Часть указанных лиц находится за пределами Российской Федерации; трансграничная передача осуществляется в объёме, необходимом для работы соответствующих сервисов.':
        'Some of these parties are located outside the Russian Federation; cross-border transfer takes place only to the extent needed for those services to work.',
    '8. Сроки хранения': '8. Retention periods',
    'Обезличенные данные о посещениях хранятся в сервисе веб-аналитики в течение срока, установленного этим сервисом. Переписка с посетителем хранится до достижения цели обработки, а после — до момента отзыва согласия либо удаления переписки.':
        'Anonymised visit data is kept by the analytics service for the period that service defines. Correspondence with a visitor is kept until the purpose of processing is met, and after that until consent is withdrawn or the correspondence is deleted.',
    '9. Права посетителя': '9. Your rights',
    'Вы вправе получить сведения об обработке ваших персональных данных, потребовать их уточнения, блокирования или уничтожения, а также отозвать согласие на обработку. Для этого направьте запрос на адрес':
        'You may obtain information about the processing of your personal data, request its correction, blocking or deletion, and withdraw your consent. To do so, send a request to',
    'с описанием требования. Оператор отвечает в течение 30 дней с момента получения запроса.':
        'describing what you need. The Operator responds within 30 days of receiving the request.',
    'Если вы считаете, что ваши права нарушены, вы можете обратиться в Роскомнадзор как уполномоченный орган по защите прав субъектов персональных данных.':
        'If you believe your rights have been violated, you may contact Roskomnadzor, the authority protecting the rights of data subjects.',
    '10. Защита данных': '10. Data protection',
    'Оператор принимает разумные организационные и технические меры для защиты персональных данных от неправомерного доступа, уничтожения, изменения и распространения. Доступ к данным веб-аналитики защищён учётной записью Оператора с двухфакторной аутентификацией.':
        'The Operator takes reasonable organisational and technical measures to protect personal data from unauthorised access, destruction, alteration and disclosure. Access to analytics data is protected by the Operator’s account with two-factor authentication.',
    '11. Изменения Политики': '11. Changes to this Policy',
    'Оператор вправе изменять настоящую Политику. Действующая редакция всегда размещена на этой странице; дата редакции указана в начале документа.':
        'The Operator may amend this Policy. The current version is always published on this page; the version date is shown at the top.',
    '12. Контакты': '12. Contact',
    'Вопросы по обработке персональных данных:': 'Questions about personal data processing:',
    'либо': 'or',
    'в Telegram.': 'on Telegram.',
    '← Вернуться на главную': '← Back to the homepage',

    # ---------- заметка: что автоматизировать первым ----------
    'Что автоматизировать первым, если бюджет один — Митин Михаил':
        'What to automate first when you can afford one thing — Mikhail Mitin',
    'Процессы ·': 'Processes ·',
    '22 июля 2026': '22 July 2026',
    'Считайте не задачи, а часы': 'Count hours, not tasks',
    'Обычно автоматизировать хотят то, что раздражает. Но раздражает не всегда то, что дорого стоит. Возьмите неделю и выпишите повторяющиеся действия сотрудников с честной оценкой времени: скопировать заявку в таблицу — 3 минуты, но сорок раз в день.':
        'People usually want to automate whatever annoys them. But the annoying thing is not always the expensive one. Take a week and write down the repetitive actions your staff perform, with an honest time estimate: copying an enquiry into a spreadsheet takes 3 minutes — forty times a day.',
    'Формула, которой хватает': 'A formula that is good enough',
    'Умножьте время одной операции на количество повторов в месяц и на стоимость часа сотрудника. Получится сумма, которую процесс съедает. Сравните её с ценой автоматизации — и вы увидите срок окупаемости в месяцах. Всё, что окупается быстрее полугода, стоит делать не раздумывая.':
        'Multiply the time of one operation by how often it repeats per month and by the hourly cost of the employee. That is what the process eats. Compare it with the cost of automation and you get the payback period in months. Anything that pays back in under six months is worth doing without further thought.',
    'Три места, где почти всегда есть деньги': 'Three places where the money almost always is',
    'Перенос данных между системами руками: сайт → таблица → CRM → бухгалтерия.':
        'Moving data between systems by hand: website → spreadsheet → CRM → accounting.',
    'Ответы на одинаковые вопросы клиентов: график, цены, статус заказа.':
        'Answering the same client questions: opening hours, prices, order status.',
    'Регулярные отчёты, которые кто-то собирает по утрам из трёх источников.':
        'Recurring reports someone assembles every morning from three sources.',
    'Чего делать не надо': 'What not to do',
    'Не автоматизируйте процесс, который сам по себе кривой. Если заявки теряются, потому что нет правила, кто их обрабатывает, робот будет терять их быстрее и в больших количествах. Сначала процесс, потом код.':
        'Do not automate a process that is broken to begin with. If enquiries get lost because no one owns them, a robot will lose them faster and in larger numbers. Process first, code second.',
    'И не начинайте с самого сложного, даже если оно самое болезненное. Первая автоматизация должна дать результат за две-три недели: команда увидит пользу и перестанет сопротивляться следующей.':
        'And do not start with the hardest thing, even if it hurts most. The first automation should show a result in two or three weeks: the team sees the benefit and stops resisting the next one.',
    'Как понять, что получилось': 'How to tell whether it worked',
    'До старта зафиксируйте цифру: сколько часов в месяц уходит и сколько заявок теряется. Через месяц после запуска сравните. Без замера «до» любая автоматизация превращается в вопрос веры, а вера заканчивается ровно тогда, когда что-нибудь ломается.':
        'Before you start, write down the number: how many hours a month it takes and how many enquiries are lost. Compare a month after launch. Without a “before” measurement, automation becomes a matter of faith — and faith runs out the moment something breaks.',
    '← Все заметки': '← All notes',
    'Нужна помощь с задачей?': 'Need a hand with your task?',

    # ---------- список заметок ----------
    'Заметки об автоматизации, ботах и сайтах — Митин Михаил':
        'Notes on automation, bots and websites — Mikhail Mitin',
    'Разборы вопросов, которые чаще всего задают заказчики: сколько стоит бот, что автоматизировать первым, MAX или Telegram.':
        'Answers to the questions clients ask most: what a bot costs, what to automate first, MAX or Telegram.',
    'Короткие разборы вопросов, которые всплывают в переписке с каждым вторым клиентом: сколько это стоит, с чего начинать и что выбрать.':
        'Short answers to the questions that come up with every other client: what it costs, where to start and what to choose.',
    'Деньги ·': 'Money ·',
    '14 августа 2026': '14 August 2026',
    'Мессенджеры ·': 'Messengers ·',
    '30 июня 2026': '30 June 2026',
    '← На главную': '← Back to the homepage',
    'Есть задача?': 'Got a task in mind?',

    # ---------- заметка: MAX или Telegram ----------
    'MAX или Telegram: где делать бота для бизнеса — Митин Михаил':
        'MAX or Telegram: where to build a business bot — Mikhail Mitin',
    'Вопрос не в платформе, а в том, где ваши клиенты':
        'The question is not the platform, it is where your clients are',
    'Бот живёт там, куда человек и так заходит десять раз в день. Если ваша аудитория переписывается с вами в Telegram — начинать надо там. Если значительная часть клиентов уже перешла в MAX, бот в Telegram их просто не увидит.':
        'A bot lives where people already go ten times a day. If your audience messages you on Telegram, start there. If a large share of your clients has moved to MAX, a Telegram bot simply will not see them.',
    'Что важно для разработки': 'What matters for development',
    'С точки зрения кода различия сводятся к API: набор методов, формат кнопок, правила рассылок и лимиты. Логика процесса — запись, оплата, выгрузка в CRM — остаётся одной и той же. Поэтому второй бот почти всегда дешевле первого: переписывается слой общения с мессенджером, а не всё приложение.':
        'In code terms the differences come down to the API: the set of methods, button formats, broadcast rules and limits. The process logic — booking, payment, CRM export — stays the same. That is why a second bot is almost always cheaper than the first: you rewrite the messenger layer, not the whole application.',
    'Практический подход': 'A practical approach',
    'Проектируйте логику отдельно от мессенджера — тогда перенос будет стоить дёшево.':
        'Design the logic separately from the messenger — then porting is cheap.',
    'Начните с одной платформы, где аудитория уже есть, и посмотрите на цифры.':
        'Start with the one platform where your audience already is, and look at the numbers.',
    'Вторую добавляйте, когда первая приносит заявки: так вы платите за расширение, а не за эксперимент.':
        'Add the second once the first brings enquiries: then you are paying for expansion, not an experiment.',
    'Когда нужны обе сразу': 'When you need both at once',
    'Если вы работаете с широкой розничной аудиторией и не можете позволить себе потерять часть клиентов из-за выбора мессенджера. В этом случае имеет смысл сразу заложить общий сервис, к которому подключаются оба бота, — иначе через полгода у вас будет две несвязанные системы и две базы клиентов.':
        'If you serve a broad retail audience and cannot afford to lose part of it to a messenger choice. In that case design a shared service both bots plug into from the start — otherwise in six months you will have two disconnected systems and two client databases.',
    'Короткий вывод': 'The short version',
    'Платформа — это витрина, а не суть. Стройте автоматизацию так, чтобы смена или добавление мессенджера занимали неделю, а не переписывание проекта с нуля.':
        'The platform is a shop window, not the substance. Build automation so that switching or adding a messenger takes a week, not a rewrite from scratch.',

    # ---------- заметка: сколько стоит бот ----------
    'Сколько стоит Telegram-бот и из чего складывается цена — Митин Михаил':
        'What a Telegram bot costs and what makes up the price — Mikhail Mitin',
    'Цену определяет не бот, а то, что за ним': 'The price is set by what is behind the bot',
    'Сам диалог — самая дешёвая часть работы. Меню, кнопки и ответы на вопросы можно собрать за пару дней. Деньги начинаются там, где бот перестаёт быть автоответчиком: когда он должен знать расписание, помнить клиента, списывать оплату и класть заявку туда, где её увидит менеджер.':
        'The dialogue itself is the cheapest part. Menus, buttons and answers can be assembled in a couple of days. The money starts where the bot stops being an autoresponder: when it has to know the schedule, remember the client, take payment and put the enquiry where a manager will see it.',
    'Поэтому вопрос «сколько стоит бот» без описания процесса — как вопрос «сколько стоит машина». Ответ будет от 40 тысяч до бесконечности, и оба варианта окажутся правдой.':
        'So asking “what does a bot cost” without describing the process is like asking “what does a car cost”. The answer runs from ₽40,000 to infinity, and both ends are true.',
    'Из чего складывается смета': 'What the estimate is made of',
    'Сценарий диалога: сколько развилок, что делать, если пользователь свернул не туда.':
        'The dialogue script: how many branches, and what happens when the user takes a wrong turn.',
    'Хранение данных: нужна ли база, или хватит таблицы.':
        'Data storage: do you need a database or will a spreadsheet do.',
    'Интеграции: каждая связь с чужим сервисом — отдельная работа, и не всегда предсказуемая.':
        'Integrations: every link to someone else’s service is separate work, and not always predictable.',
    'Оплата: приём платежей поднимает цену заметно, потому что там нельзя ошибаться.':
        'Payments: accepting money raises the price noticeably, because there you cannot afford mistakes.',
    'Админ-часть: кто-то же должен видеть заявки и менять расписание.':
        'The admin side: someone has to see the enquiries and change the schedule.',
    'Запуск и передача: сервер, домен, доступы, инструкция для команды.':
        'Launch and handover: server, domain, accounts, a manual for the team.',
    'Ориентиры': 'Ballpark figures',
    'Бот, который принимает заявки и складывает их в таблицу, — 40–70 тысяч. Бот с записью, расписанием и напоминаниями — 80–150. Бот с оплатой, личным кабинетом и синхронизацией с CRM — от 150 и выше. Это вилки, а не прайс: точная цифра появляется после разбора процесса.':
        'A bot that takes enquiries and drops them into a spreadsheet: ₽40,000–70,000. A bot with booking, scheduling and reminders: ₽80,000–150,000. A bot with payments, a user account and CRM sync: ₽150,000 and up. These are ranges, not a price list: the exact figure appears after reviewing the process.',
    'На чём экономить можно': 'Where you can save',
    'На красоте. Боту не нужен уникальный дизайн: пользователь видит стандартные кнопки мессенджера. На редких сценариях — их можно добавить потом, когда станет ясно, нужны ли они вообще. На собственной админ-панели: на старте часто хватает Google Таблицы, которую бот заполняет сам.':
        'On looks. A bot needs no unique design: the user sees the messenger’s standard buttons. On rare scenarios — add them later, once it is clear they are needed at all. On a custom admin panel: at the start a Google Sheet the bot fills in itself is often enough.',
    'На чём экономить не стоит': 'Where you should not save',
    'На обработке ошибок. Разница между ботом за 40 тысяч и ботом за 120 часто именно в этом: первый молча теряет заявку, если чужой сервис не ответил, второй повторит запрос и напишет вам в чат. Вторая статья — передача доступов. Если код и токены остались у исполнителя, вы не владелец бота, а арендатор.':
        'On error handling. The difference between a ₽40,000 bot and a ₽120,000 one is often exactly this: the first silently loses an enquiry when another service does not respond, the second retries and messages you in chat. The second item is handover. If the code and tokens stay with the contractor, you are not the bot’s owner but its tenant.',
    'Что делать с этим знанием': 'What to do with all this',
    'Перед тем как спрашивать цену, опишите процесс: кто, что и в каком порядке делает руками сегодня. С таким описанием разработчик назовёт вилку сразу, а вы сможете сравнить предложения между собой, а не гадать, почему они отличаются втрое.':
        'Before asking for a price, describe the process: who does what, by hand, in what order, today. With that description a developer can give you a range straight away — and you can compare offers instead of guessing why they differ threefold.',
}
