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

  var cta = document.querySelector('.mobile-cta');
  var hero = document.querySelector('.hero');
  var contacts = document.getElementById('contacts');

  if (cta && hero && contacts && 'IntersectionObserver' in window) {
    var heroVisible = true;
    var contactsVisible = false;

    var update = function () {
      cta.classList.toggle('is-shown', !heroVisible && !contactsVisible);
    };

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

  /* ---- 4. Диалог с ботом на первом экране ----
     Реплики лежат в разметке, здесь они показываются по очереди.
     Перед ответами бота мигают три точки. Проигрывается один раз,
     когда мокап попадает в поле зрения. */

  var log = document.querySelector('.chat__log');

  if (log) {
    var msgs = Array.prototype.slice.call(log.children);

    var mount = function (el) {
      el.classList.add('is-mounted');
      requestAnimationFrame(function () {
        requestAnimationFrame(function () { el.classList.add('is-shown'); });
      });
    };

    if (reduceMotion || !('IntersectionObserver' in window)) {
      msgs.forEach(mount);
    } else {
      var typing = document.createElement('li');
      typing.className = 'msg msg--out msg--typing';
      typing.innerHTML = '<i></i><i></i><i></i>';

      var step = function (i) {
        if (i >= msgs.length) { return; }

        var el = msgs[i];
        var fromBot = el.classList.contains('msg--out');
        var pause = i === 0 ? 500 : 800;

        setTimeout(function () {
          if (!fromBot) {
            mount(el);
            step(i + 1);
            return;
          }
          log.appendChild(typing);
          mount(typing);
          setTimeout(function () {
            if (typing.parentNode) { typing.parentNode.removeChild(typing); }
            typing.classList.remove('is-mounted', 'is-shown');
            mount(el);
            step(i + 1);
          }, 850);
        }, pause);
      };

      var chatObserver = new IntersectionObserver(function (entries, obs) {
        if (entries[0].isIntersecting) {
          obs.disconnect();
          step(0);
        }
      }, { threshold: 0.25 });

      chatObserver.observe(log);
    }
  }

  /* ---- 5. Яндекс.Метрика ----
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

  /* ---- 6. Год в подвале ---- */

  var year = document.getElementById('year');
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
