document.addEventListener('DOMContentLoaded', function() {
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  var elems = document.querySelectorAll('.materialboxed');
  var instances = M.Materialbox.init(elems, options);
});