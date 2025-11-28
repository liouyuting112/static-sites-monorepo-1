document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger-btn');
    const navLinks = document.querySelector('.nav-links');
    const dropdowns = document.querySelectorAll('.dropdown');

    function toggleMenu() {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
    }

    burger.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMenu();
    });

    // Mobile Dropdown Handling
    dropdowns.forEach(dd => {
        dd.addEventListener('click', (e) => {
            if (window.innerWidth < 769) {
                // If clicking the text itself (which is likely a link or span), toggle menu
                const menu = dd.querySelector('.dropdown-menu');
                if (menu) {
                    dd.classList.toggle('active');
                    // Prevent navigation if it's a link, unless we want double tap behavior?
                    // Requirement: Mobile dropdown width 100% centered.
                    // Usually clicking the parent expands it.
                }
            }
        });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
        if (navLinks.classList.contains('active') && 
            !navLinks.contains(e.target) && 
            !burger.contains(e.target)) {
            toggleMenu();
        }
    });

    // Close on link click
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
           if(navLinks.classList.contains('active')) toggleMenu();
        });
    });
});

