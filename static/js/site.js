// THE BASS ROOM: close the mobile menu after selecting a page.
document.addEventListener('DOMContentLoaded', function () {
  var nav = document.getElementById('mainNav');
  if (!nav || typeof bootstrap === 'undefined') return;
  nav.querySelectorAll('a.nav-link').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth < 992 && nav.classList.contains('show')) {
        bootstrap.Collapse.getOrCreateInstance(nav).hide();
      }
    });
  });
});
