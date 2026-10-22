/* WiseQ shared catalog renderer — single source for all three concept versions.
   Any element with [data-render] gets populated from window.WISEQ_PRODUCTS:
     data-render="grid"  → family-grouped card grid   (V1/V3 full catalog)
     data-render="table" → printed-table rows          (V2 appendix)
     data-render="rail"  → hero-pick horizontal rail   (V1 pan act; data-max=N)
   Helpers (esc/eur/link) are defined once here; pages only contribute CSS. */
(function () {
  if (!window.WISEQ_PRODUCTS) return;
  var products = window.WISEQ_PRODUCTS;

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  }
  function eur(v) {
    var n = typeof v === 'number' ? v : parseFloat(v);
    return '€ ' + n.toFixed(2).replace('.', ',');
  }
  function link(p) { return 'https://www.wiseq.nl/products/' + p.h; }

  var famOrder = ['koptelefoons', 'smartwatches', 'tablets', 'opladen-opberg', 'kabels', 'accessoires', 'samples'];
  var famName = {
    koptelefoons: 'Koptelefoons', smartwatches: 'Smartwatches', tablets: 'Tablets',
    'opladen-opberg': 'Opladen & opbergen', kabels: 'Kabels', accessoires: 'Accessoires', samples: 'Proefexemplaren'
  };

  /* ---- rail: one hero per family, then distinct fillers up to max ---- */
  function renderRail(host) {
    var max = parseInt(host.getAttribute('data-max') || '14', 10);
    var seen = {}, pick = [];
    products.forEach(function (p) {
      if (!seen[p.f] && p.img_local && parseFloat(p.p) > 0) { seen[p.f] = 1; pick.push(p); }
    });
    products.forEach(function (p) {
      if (pick.length < max && pick.indexOf(p) < 0 && p.img_local && parseFloat(p.p) > 0) pick.push(p);
    });
    var frag = document.createDocumentFragment();
    pick.forEach(function (p) {
      var a = document.createElement('a');
      a.className = 'obj';
      a.href = link(p);
      a.target = '_blank';
      a.rel = 'noopener';
      a.setAttribute('data-sc-tilt', '6');
      // NOTE: all fields are first-party (our products.js); titles escaped via esc().
      a.innerHTML =
        '<div class="ph"><img loading="lazy" src="../' + esc(p.img_local) + '" alt="' + esc(p.t) + '"></div>' +
        '<span class="sc-label">' + esc(p.t) + '</span><span class="cap">' + eur(p.p) + '</span>';
      frag.appendChild(a);
    });
    host.appendChild(frag);
    host.setAttribute('data-count', String(pick.length));
  }

  /* ---- table: printed appendix rows ---- */
  function renderTable(mount) {
    var tbody = mount.tagName === 'TBODY' ? mount : mount.querySelector('tbody');
    if (!tbody) return;
    var frag = document.createDocumentFragment();
    products.forEach(function (p) {
      if (parseFloat(p.p) === 0) return; // samples/stuks: geen prijsloze rijen
      var tr = document.createElement('tr');
      tr.setAttribute('data-sc-in', '');
      tr.innerHTML =
        '<td><img class="thumb" loading="lazy" src="../' + p.img_local + '" alt=""></td>' +
        '<td class="n">' + esc(p.t) + '</td>' +
        '<td>' + famName[p.f] + '</td>' +
        '<td>—</td>' +
        '<td class="p">' + eur(p.p) + '</td>';
      frag.appendChild(tr);
    });
    tbody.appendChild(frag);
    mount.setAttribute('data-count', String(tbody.children.length));
  }

  /* ---- grid: family-grouped cards ---- */
  function renderGrid(mount) {
    var wrap = document.createDocumentFragment();
    famOrder.forEach(function (f) {
      var items = products.filter(function (p) { return p.f === f && parseFloat(p.p) > 0; });
      if (!items.length) return;
      var h = document.createElement('p');
      h.className = 'cat-family';
      h.setAttribute('data-sc-in', '');
      h.textContent = famName[f] + ' — ' + items.length + ' producten';
      wrap.appendChild(h);
      var g = document.createElement('div');
      g.className = 'cat-grid';
      items.forEach(function (p) {
        var a = document.createElement('a');
        a.className = 'cat-item';
        a.href = link(p);
        a.target = '_blank';
        a.rel = 'noopener';
        a.setAttribute('data-sc-in', '');
        a.innerHTML =
          '<span class="im"><img loading="lazy" src="../' + p.img_local + '" alt=""></span>' +
          '<span class="meta"><b>' + esc(p.t).slice(0, 64) + '</b><i>' + eur(p.p) + '</i></span>';
        g.appendChild(a);
      });
      wrap.appendChild(g);
    });
    mount.appendChild(wrap);
    mount.setAttribute('data-count', String(mount.querySelectorAll('.cat-item').length));
  }

  /* ---- dispatch over every [data-render] mount on the page ---- */
  var mounts = document.querySelectorAll('[data-render]');
  for (var i = 0; i < mounts.length; i++) {
    var m = mounts[i], mode = m.getAttribute('data-render');
    if (m.getAttribute('data-count') !== null) continue; // already rendered
    if (mode === 'table') renderTable(m);
    else if (mode === 'rail') renderRail(m);
    else renderGrid(m);
  }
})();
