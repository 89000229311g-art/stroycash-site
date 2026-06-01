/* ================================================================
   СтройКэш — custom.js v3
   ================================================================ */
(function () {
  'use strict';

  /* ── Определяем: есть ли уже Tilda-мессенджеры на странице ── */
  function hasTildaMessengers() {
    // Tilda использует t898__icon для мессенджер-виджетов
    // Проверяем после небольшой задержки (Tilda рендерит async)
    return !!(
      document.querySelector('.t898__icon') ||
      document.querySelector('[class*="t-widgetman"]') ||
      document.querySelector('[class*="widgetman"]')
    );
  }

  /* ── 1. ДОБАВЛЯЕМ «БЛОГ» В TILDA-МЕНЮ ─────────────────── */
  function injectBlogLink() {
    var SELECTORS = ['.t450__list', '.t-menu__list', '.t978__menu-list', '.t794__list'];
    for (var i = 0; i < SELECTORS.length; i++) {
      var list = document.querySelector(SELECTORS[i]);
      if (!list) continue;
      if (list.querySelector('[href="/blog"]')) return;
      var existingLink = list.querySelector('a');
      var fs = '18px', fw = '500', fc = '#494949', ff = "'Gilroy',Arial,sans-serif";
      if (existingLink) {
        var cs = window.getComputedStyle(existingLink);
        fs = cs.fontSize || fs;
        fw = cs.fontWeight || fw;
        fc = cs.color || fc;
        ff = cs.fontFamily || ff;
      }
      var link = document.createElement('a');
      link.href = '/blog';
      link.className = existingLink ? existingLink.className : 't-menu__link-item';
      link.textContent = 'Блог';
      link.style.cssText = 'font-family:' + ff + ';font-size:' + fs + ';font-weight:' + fw + ';color:' + fc + ';';
      list.appendChild(link);
      return;
    }
  }

  function addBlogToMenu() {
    var done = false;
    function tryInject() {
      if (done) return;
      injectBlogLink();
      if (document.querySelector('[href="/blog"]')) done = true;
    }
    tryInject();
    if (done) return;
    if ('MutationObserver' in window) {
      var obs = new MutationObserver(function() { tryInject(); if (done) obs.disconnect(); });
      obs.observe(document.body, { childList: true, subtree: true });
      setTimeout(function() { obs.disconnect(); }, 10000);
    } else {
      var t = setInterval(function() { tryInject(); if (done) clearInterval(t); }, 300);
      setTimeout(function() { clearInterval(t); }, 10000);
    }
  }

  /* ── 2. FLOATING КНОПКИ ──────────────────────────────────
     Логика:
     - Tilda-страницы: у них уже есть WA+TG в шаблоне (t898)
       → показываем только кнопку «Наверх»
     - Блог/статьи (наши страницы): WA+TG нет
       → показываем полный набор WA + TG + «Наверх»
  ────────────────────────────────────────────────────────── */
  function initFloat() {
    var wrap = document.createElement('div');
    wrap.id = 'sc-float';

    // WA + TG — только если Tilda не добавила их сама
    // Проверяем через 1.5 сек (Tilda рендерит виджеты async)
    var WA_SVG = '<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>';
    var TG_SVG = '<svg viewBox="0 0 24 24"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>';
    var UP_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round"><polyline points="18 15 12 9 6 15"/></svg>';

    // Кнопка наверх — всегда
    var topBtn = document.createElement('button');
    topBtn.id = 'sc-to-top';
    topBtn.className = 'sc-float-btn sc-float-btn--top';
    topBtn.setAttribute('aria-label', 'Наверх');
    topBtn.innerHTML = UP_SVG;
    wrap.appendChild(topBtn);

    document.body.appendChild(wrap);

    // WA + TG добавляем только если Tilda не дала своих (проверка через 1.5 сек)
    setTimeout(function() {
      if (!hasTildaMessengers()) {
        var wa = document.createElement('a');
        wa.href = 'https://wa.me/79303346176';
        wa.target = '_blank';
        wa.rel = 'noopener';
        wa.setAttribute('aria-label', 'WhatsApp');
        wa.className = 'sc-float-btn sc-float-btn--wa';
        wa.innerHTML = WA_SVG;

        var tg = document.createElement('a');
        tg.href = 'https://t.me/stroycash_remont';
        tg.target = '_blank';
        tg.rel = 'noopener';
        tg.setAttribute('aria-label', 'Telegram');
        tg.className = 'sc-float-btn sc-float-btn--tg';
        tg.innerHTML = TG_SVG;

        // Вставляем перед кнопкой наверх
        wrap.insertBefore(tg, topBtn);
        wrap.insertBefore(wa, tg);
      }
    }, 1500);

    // Скролл — показываем/скрываем кнопку наверх
    window.addEventListener('scroll', function () {
      topBtn.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });
    topBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ── 3. ПРОГРЕСС-БАР (только на статьях) ──────────────── */
  function initReadingProgress() {
    if (!document.querySelector('.sc-article')) return;
    var wrap = document.createElement('div');
    wrap.id = 'sc-reading-progress';
    var bar = document.createElement('div');
    bar.id = 'sc-reading-progress-bar';
    wrap.appendChild(bar);
    document.body.prepend(wrap);
    window.addEventListener('scroll', function () {
      var total = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (total > 0 ? (window.scrollY / total) * 100 : 0) + '%';
    }, { passive: true });
  }

  /* ── 4. SCROLL REVEAL (только на статьях) ──────────────── */
  function initScrollReveal() {
    if (!document.querySelector('.sc-article')) return;
    if (!('IntersectionObserver' in window)) return;
    document.querySelectorAll(
      '.sc-article h2, .sc-infobox, .sc-warn, .sc-steps li, .sc-faq-item, .sc-table'
    ).forEach(function (el) { el.classList.add('sc-reveal'); });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('sc-visible'); obs.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -50px 0px' });
    document.querySelectorAll('.sc-reveal').forEach(function (el) { obs.observe(el); });
  }

  /* ── 5. PRECONNECT для Tilda CDN ───────────────────────── */
  function addPreconnects() {
    ['https://ws.tildacdn.com', 'https://neo.tildacdn.com', 'https://static.tildacdn.com'].forEach(function (url) {
      if (document.querySelector('link[href="' + url + '"]')) return;
      var l = document.createElement('link');
      l.rel = 'preconnect'; l.href = url; l.crossOrigin = 'anonymous';
      document.head.appendChild(l);
    });
  }

  /* ── INIT ─────────────────────────────────────────────── */
  function init() {
    addPreconnects();
    initFloat();
    initReadingProgress();
    initScrollReveal();
    addBlogToMenu();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
