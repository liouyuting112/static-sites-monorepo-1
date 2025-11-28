document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');
    const dropdowns = document.querySelectorAll('.dropdown');

    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
    });

    // Mobile Dropdown
    dropdowns.forEach(dd => {
        dd.addEventListener('click', (e) => {
            if (window.innerWidth < 769) {
                dd.classList.toggle('active');
            }
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navLinks.contains(e.target) && !burger.contains(e.target)) {
            navLinks.classList.remove('active');
        }
    });
});

