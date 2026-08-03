/* Tri-Valley Long Term Care — site behaviour.
   Everything here is progressive enhancement: with JavaScript off, the nav is
   a plain list, every directory listing is visible, and checklists are still
   usable on paper. */
(function () {
  'use strict';

  document.documentElement.classList.add('is-ready');

  /* ------------------------------------------------------------ nav ---- */
  var toggle = document.querySelector('[data-navtoggle]');
  var nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.hidden = false;
    toggle.addEventListener('click', function () {
      var open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') {
        nav.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ------------------------------------------------------- checklists -- */
  /* Families are told throughout this guide to keep records. The checklists
     remember what you ticked so you can come back and print them. */
  var STORE = 'tvltc.checks.v1';

  function readState() {
    try { return JSON.parse(localStorage.getItem(STORE) || '{}'); }
    catch (err) { return {}; }
  }
  function writeState(state) {
    try { localStorage.setItem(STORE, JSON.stringify(state)); }
    catch (err) { /* private browsing — checklist still works for this visit */ }
  }

  var state = readState();

  Array.prototype.forEach.call(document.querySelectorAll('[data-check]'), function (block) {
    var boxes = block.querySelectorAll('input[type="checkbox"]');
    var tally = block.querySelector('[data-tally]');
    var count = block.querySelector('[data-count]');
    var verdict = block.querySelector('[data-verdict]');
    var trigger = parseInt(block.getAttribute('data-trigger') || '0', 10);
    var triggerText = block.getAttribute('data-trigger-text') || '';
    var restText = verdict ? verdict.textContent : '';

    function update() {
      var n = 0;
      Array.prototype.forEach.call(boxes, function (box) {
        if (box.checked) { n++; }
      });
      if (count) {
        count.textContent = n + ' of ' + boxes.length;
      }
      if (verdict && trigger) {
        var hit = n >= trigger;
        verdict.textContent = hit ? triggerText : restText;
        verdict.setAttribute('data-triggered', String(hit));
      }
      if (tally) { tally.hidden = false; }
    }

    Array.prototype.forEach.call(boxes, function (box) {
      if (state[box.id]) { box.checked = true; }
      box.addEventListener('change', function () {
        state[box.id] = box.checked;
        writeState(state);
        update();
      });
    });

    update();

    var printBtn = block.querySelector('[data-print]');
    if (printBtn) {
      printBtn.hidden = false;
      printBtn.addEventListener('click', function () { window.print(); });
    }
    var clearBtn = block.querySelector('[data-clear]');
    if (clearBtn) {
      clearBtn.hidden = false;
      clearBtn.addEventListener('click', function () {
        Array.prototype.forEach.call(boxes, function (box) {
          box.checked = false;
          state[box.id] = false;
        });
        writeState(state);
        update();
      });
    }
  });

  /* -------------------------------------------------------- directory -- */
  var dir = document.querySelector('[data-directory]');
  if (dir) {
    var listings = Array.prototype.slice.call(dir.querySelectorAll('[data-listing]'));
    var search = dir.querySelector('[data-search]');
    var citySel = dir.querySelector('[data-city]');
    var chips = Array.prototype.slice.call(dir.querySelectorAll('[data-chip]'));
    var out = dir.querySelector('[data-count-results]');
    var empty = dir.querySelector('[data-empty]');
    var reset = dir.querySelector('[data-reset]');
    var activeCat = '';

    function apply() {
      var q = (search && search.value || '').trim().toLowerCase();
      var city = (citySel && citySel.value) || '';
      var shown = 0;

      listings.forEach(function (el) {
        var haystack = el.getAttribute('data-text') || '';
        var cats = el.getAttribute('data-cats') || '';
        var elCity = el.getAttribute('data-city') || '';
        var ok = (!q || haystack.indexOf(q) !== -1) &&
                 (!activeCat || cats.indexOf('|' + activeCat + '|') !== -1) &&
                 (!city || elCity === city);
        el.hidden = !ok;
        if (ok) { shown++; }
      });

      if (out) { out.textContent = String(shown); }
      if (empty) { empty.hidden = shown !== 0; }
    }

    if (search) { search.addEventListener('input', apply); }
    if (citySel) { citySel.addEventListener('change', apply); }

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var value = chip.getAttribute('data-chip');
        activeCat = (activeCat === value) ? '' : value;
        chips.forEach(function (c) {
          c.setAttribute('aria-pressed', String(c.getAttribute('data-chip') === activeCat));
        });
        apply();
      });
    });

    if (reset) {
      reset.addEventListener('click', function () {
        if (search) { search.value = ''; }
        if (citySel) { citySel.value = ''; }
        activeCat = '';
        chips.forEach(function (c) { c.setAttribute('aria-pressed', 'false'); });
        apply();
        if (search) { search.focus(); }
      });
    }

    apply();
  }

  /* ----------------------------------------------------------- cookie -- */
  var cookie = document.querySelector('[data-cookie]');
  if (cookie) {
    var KEY = 'tvltc.cookies.v1';
    var choice = null;
    try { choice = localStorage.getItem(KEY); } catch (err) { choice = 'skip'; }
    if (!choice) {
      cookie.hidden = false;
      Array.prototype.forEach.call(cookie.querySelectorAll('[data-cookie-choice]'), function (btn) {
        btn.addEventListener('click', function () {
          try { localStorage.setItem(KEY, btn.getAttribute('data-cookie-choice')); } catch (err) { /* noop */ }
          cookie.hidden = true;
        });
      });
    }
  }

  /* ------------------------------------------------------------ forms -- */
  /* No back end yet. Rather than silently drop a family's message, the form
     says plainly what to do instead. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-form]'), function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('[data-form-status]');
      if (status) {
        status.hidden = false;
        status.focus();
      }
    });
  });
})();
