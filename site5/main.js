document.addEventListener('DOMContentLoaded', () => {
    // Menu
    const burger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav-links');
    
    if (burger) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // Mobile Dropdown
    const drops = document.querySelectorAll('.dropdown');
    drops.forEach(d => {
        d.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                if (e.target.tagName !== 'A' || e.target.getAttribute('href') === '#') {
                    e.preventDefault();
                    d.classList.toggle('active');
                }
            }
        });
    });

    // Date
    const daily = document.getElementById('daily-link');
    if (daily) daily.href = 'articles/2025-11-28.html';

    // Clickable cards logic
    document.querySelectorAll('.memory-card').forEach(card => {
        card.addEventListener('click', (e) => {
            const link = card.querySelector('a');
            if (link && e.target !== link) {
                link.click();
            }
        });
    });
});

