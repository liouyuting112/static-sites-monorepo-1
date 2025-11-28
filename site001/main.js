document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navMenu = document.querySelector('.nav-menu');
    const dropdowns = document.querySelectorAll('.dropdown');

    // Toggle Mobile Menu
    burger.addEventListener('click', (e) => {
        e.stopPropagation();
        navMenu.classList.toggle('active');
        burger.classList.toggle('toggle');
    });

    // Mobile Dropdown Toggle
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            if (window.innerWidth < 769) {
                // Prevent immediate navigation for parent link on mobile if it has submenu
                // Actually, the requirement says "Select Options" so the parent might be text only or a link.
                // Assuming the parent is a span or link.
                const content = dropdown.querySelector('.dropdown-content');
                if (content) {
                   // e.preventDefault(); // If we want to force click to open
                   dropdown.classList.toggle('active');
                }
            }
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!navMenu.contains(e.target) && !burger.contains(e.target)) {
            navMenu.classList.remove('active');
            burger.classList.remove('toggle');
        }
    });

    // Close menu when clicking a link
    navMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            burger.classList.remove('toggle');
        });
    });
});

