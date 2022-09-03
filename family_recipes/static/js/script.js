document.addEventListener('DOMContentLoaded', function() {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  let hero = document.querySelectorAll('.materialboxed');
  M.Materialbox.init(hero);

  let elems = document.querySelectorAll('.modal');
  M.Modal.init(elems);
});