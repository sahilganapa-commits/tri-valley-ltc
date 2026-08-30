/* Tri-Valley Long Term Care, site behaviour.
   Everything here is progressive enhancement: with JavaScript off, the nav is
   a plain list, every directory listing is visible, and checklists are still
   usable on paper. */
(function () {
  'use strict';

  document.documentElement.classList.add('is-ready');

  // Shown as the fallback whenever a form post fails.
  var CONTACT_EMAIL = 'hello@trivalleyltc.org';

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

  /* ------------------------------- sticky header past the hero -------- */
  /* The bar rides transparently on the hero photograph, then detaches and
     follows the reader as a solid bar once the photo has scrolled by. */
  var overlayBar = document.querySelector('[data-masthead]');
  var coverHero = document.querySelector('.hero--cover');
  if (overlayBar && coverHero) {
    var stuck = false;
    var sync = function () {
      var past = coverHero.getBoundingClientRect().bottom <= 0;
      if (past !== stuck) {
        stuck = past;
        overlayBar.classList.toggle('is-stuck', stuck);
      }
    };
    // Called straight from the scroll event: it reads one rect and flips one
    // class, so it is cheap enough not to need frame throttling, and this way
    // the final state can never be dropped with a skipped frame.
    window.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
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
    catch (err) { /* private browsing, checklist still works for this visit */ }
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

    /* Every word typed has to match, and each has to match from the start of a
       word. Loose substring matching over one long string meant "care" hit
       almost every listing and a two-word query quietly matched nothing. */
    function matcher(query) {
      var terms = query.split(/\s+/).filter(Boolean).map(function (t) {
        var safe = t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        return new RegExp('(^|[^a-z0-9])' + safe, 'i');
      });
      return function (haystack) {
        return terms.every(function (re) { return re.test(haystack); });
      };
    }

    function apply() {
      var q = (search && search.value || '').trim().toLowerCase();
      var matches = q ? matcher(q) : null;
      var city = (citySel && citySel.value) || '';
      var shown = 0;

      listings.forEach(function (el) {
        var haystack = el.getAttribute('data-text') || '';
        var cats = el.getAttribute('data-cats') || '';
        var elCity = el.getAttribute('data-city') || '';
        var ok = (!matches || matches(haystack)) &&
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
      // Publish its height so the hero can reserve exactly that much space
      // instead of guessing, and reclaim it the moment the bar is dismissed.
      var setBarHeight = function () {
        var h = cookie.hidden ? 0 : cookie.getBoundingClientRect().height;
        document.documentElement.style.setProperty('--cookiebar-h', Math.round(h) + 'px');
      };
      setBarHeight();
      window.addEventListener('resize', setBarHeight);
      Array.prototype.forEach.call(cookie.querySelectorAll('[data-cookie-choice]'), function (btn) {
        btn.addEventListener('click', function () {
          try { localStorage.setItem(KEY, btn.getAttribute('data-cookie-choice')); } catch (err) { /* noop */ }
          cookie.hidden = true;
          setBarHeight();
        });
      });
    }
  }

  /* ----------------------------------------------- print open accordions -- */
  /* A closed <details> prints as just its question. Anyone printing the FAQ
     wants the answers, so open them for the print and put them back after. */
  var faqItems = document.querySelectorAll('.faq__item');
  if (faqItems.length && window.matchMedia) {
    var reopened = [];
    window.addEventListener('beforeprint', function () {
      reopened = [];
      Array.prototype.forEach.call(faqItems, function (d) {
        if (!d.open) { d.open = true; reopened.push(d); }
      });
    });
    window.addEventListener('afterprint', function () {
      reopened.forEach(function (d) { d.open = false; });
      reopened = [];
    });
  }

  /* ------------------------------------------------------------ forms -- */
  /* Posts to the form service in the background so the visitor stays on the
     page. With JavaScript off the form submits natively to the same endpoint
     and the service shows its own confirmation, nothing is lost either way. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-form]'), function (form) {
    // The status sits after the form, not inside it, so the form can be
    // removed on success while the confirmation stays.
    var status = form.parentNode.querySelector('[data-form-status]');
    var button = form.querySelector('button[type="submit"]');
    if (!status || !form.getAttribute('action')) { return; }

    function say(message, ok) {
      status.hidden = false;
      status.className = ok ? 'formdone' : 'note';
      status.innerHTML = message;
      // On success the form goes away entirely. Leaving a filled-in form on
      // screen under a small notice reads as though nothing was sent, and
      // invites people to submit a second time.
      if (ok) { form.hidden = true; }
      status.focus();
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var label = button ? button.textContent : '';
      if (button) { button.disabled = true; button.textContent = 'Sending…'; }

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          form.reset();
          say('<strong>Thank you, your message has been sent.</strong>' +
              '<span>We reply within one business day. If it is urgent, or you would rather ' +
              'speak to someone, email <a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL +
              '</a>.</span>', true);
        } else {
          return res.json().then(function (data) {
            var why = (data && data.errors) ? data.errors.map(function (x) { return x.message; }).join(', ')
                                            : 'Something went wrong at our end.';
            say('<strong>That did not send.</strong> ' + why +
                ' Please email <a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> instead.');
          });
        }
      }).catch(function () {
        say('<strong>That did not send.</strong> Check your connection, or email ' +
            '<a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> instead.');
      }).then(function () {
        if (button) { button.disabled = false; button.textContent = label; }
      });
    });
  });
})();
