/* WiseQ full-catalog renderer — all 229 real products from wiseq.nl.
   Renders into #full-catalog. data-render="grid" (cards) or "table" (rows).
   Used by all three concept versions; each page styles it in its own grammar. */
(function () {
  var mount = document.getElementById('full-catalog');
  if (!mount || !window.WISEQ_PRODUCTS) return;
  var products = window.WISEQ_PRODUCTS;
  var mode = mount.getAttribute('data-render') || 'grid';
  var famOrder = ['koptelefoons', 'smartwatches', 'tablets', 'opladen-opberg', 'kabels', 'accessoires', 'samples'];
  var famName = {
    koptelefoons: 'Koptelefoons', smartwatches: 'Smartwatches', tablets: 'Tablets',
    'opladen-opberg': 'Opladen & opbergen', kabels: 'Kabels', accessoires: 'Accessoires', samples: 'Proefexemplaren'
  };
  function eur(v) {
    return '€ ' + v.toFixed(2).replace('.', ',').replace(/,00$/, ',00');
  }

  if (mode === 'table') {
    var tbody = mount.tagName === 'TBODY' ? mount : mount.querySelector('tbody');
    if (!tbody) return;
    var frag = document.createDocumentFragment();
    products.forEach(function (p) {
      if (parseFloat(p.p) === 0) return; // samples/stuks: geen prijsloze rijen
      var tr = document.createElement('tr');
      tr.setAttribute('data-sc-in', '');
      tr.innerHTML =
        '<td><img class="thumb" loading="lazy" src="../' + p.img_local + '" alt=""></td>' +
        '<td class="n">' + p.t.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</td>' +
        '<td>' + famName[p.f] + '</td>' +
        '<td>—</td>' +
        '<td class="p">' + eur(p.p) + '</td>';
      frag.appendChild(tr);
    });
    tbody.appendChild(frag);
    mount.setAttribute('data-count', String(tbody.children.length));
    return;
  }

  // NOTE on innerHTML: all fields come from our first-party products.js (built from
  // WiseQ's public Shopify JSON). Titles are HTML-escaped above, prices are numbers
  // from our own eur(), paths are our own local filenames. No third-party strings.
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
      a.href = 'https://www.wiseq.nl/products/' + p.h;
      a.target = '_blank';
      a.rel = 'noopener';
      a.setAttribute('data-sc-in', '');
      a.innerHTML =
        '<span class="im"><img loading="lazy" src="../' + p.img_local + '" alt=""></span>' +
        '<span class="meta"><b>' + p.t.replace(/&/g, '&amp;').replace(/</g, '&lt;').slice(0, 64) + '</b>' +
        '<i>' + eur(p.p) + '</i></span>';
      g.appendChild(a);
    });
    wrap.appendChild(g);
  });
  mount.appendChild(wrap);
  mount.setAttribute('data-count', String(mount.querySelectorAll('.cat-item').length));
})();
