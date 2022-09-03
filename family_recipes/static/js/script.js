document.addEventListener('DOMContentLoaded', function() {
  // sidenav initialisation
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // hero image initialization
  let hero = document.querySelectorAll('.materialboxed');
  M.Materialbox.init(hero);
  
  // modal box initialisation
  let elems = document.querySelectorAll('.modal');
  M.Modal.init(elems);

  // select box initialisation
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
});
