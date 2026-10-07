(function () {
  var p = new URLSearchParams(location.search);
  var q = (p.get('q') || '').toLowerCase().trim();
  var tag = p.get('tag') || '';
  var cards = document.querySelectorAll('#arch-list .card');
  var shown = 0;
  cards.forEach(function (c) {
    var ok = true;
    if (q) ok = c.dataset.title.indexOf(q) > -1 || c.dataset.tags.toLowerCase().indexOf(q) > -1;
    if (ok && tag) ok = ('|' + c.dataset.tags + '|').indexOf('|' + tag + '|') > -1;
    c.style.display = ok ? '' : 'none';
    if (ok) shown++;
  });
  var info = document.getElementById('arch-info');
  if (q || tag) {
    document.getElementById('arch-title').textContent = tag ? 'Catégorie : ' + tag : 'Résultats pour « ' + (p.get('q')) + ' »';
    info.textContent = shown + ' article(s)';
  }
  document.getElementById('arch-none').hidden = shown !== 0;
  var box = document.querySelector('.search input');
  if (box && q) box.value = p.get('q');
})();
