const hamburger = document.querySelector('.hamburger');
const mobileNav = document.querySelector('.mobile-nav');

hamburger.addEventListener('click', () => {
  const open = hamburger.classList.toggle('is-open');
  mobileNav.classList.toggle('is-open', open);
  hamburger.setAttribute('aria-expanded', String(open));
});
