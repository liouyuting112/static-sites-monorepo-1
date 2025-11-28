document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navMenu = document.querySelector('.nav-menu');
    const dropdowns = document.querySelectorAll('.dropdown');

    burger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        // Simple burger animation
        burger.children[0].style.transform = navMenu.classList.contains('active') ? 'rotate(45deg) translate(5px, 5px)' : 'none';
        burger.children[1].style.opacity = navMenu.classList.contains('active') ? '0' : '1';
        burger.children[2].style.transform = navMenu.classList.contains('active') ? 'rotate(-45deg) translate(5px, -5px)' : 'none';
    });

    // Mobile Dropdown
    dropdowns.forEach(dd => {
        dd.addEventListener('click', (e) => {
            if (window.innerWidth < 769) {
                // Toggle active class on click for mobile
                dd.classList.toggle('active');
            }
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navMenu.contains(e.target) && !burger.contains(e.target)) {
            navMenu.classList.remove('active');
            // Reset burger
            burger.children[0].style.transform = 'none';
            burger.children[1].style.opacity = '1';
            burger.children[2].style.transform = 'none';
        }
    });
});

