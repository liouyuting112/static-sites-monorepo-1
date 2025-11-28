document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav');
    const dropdowns = document.querySelectorAll('.dropdown');

    burger.addEventListener('click', () => {
        nav.classList.toggle('active');
    });

    // Mobile Dropdown
    dropdowns.forEach(dd => {
        dd.addEventListener('click', (e) => {
            if (window.innerWidth < 769) {
                const menu = dd.querySelector('.dropdown-menu');
                if (menu.style.display === 'block') {
                    menu.style.display = 'none';
                } else {
                    menu.style.display = 'block';
                }
            }
        });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!nav.contains(e.target) && !burger.contains(e.target)) {
            nav.classList.remove('active');
        }
    });
});

