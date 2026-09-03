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

  /* ---- 4. Год в подвале ---- */

  var year = document.getElementById('year');
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }
})();
