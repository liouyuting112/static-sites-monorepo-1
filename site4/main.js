document.addEventListener('DOMContentLoaded', () => {
    // Nav logic
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    
    if (burger) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // Dropdown mobile toggle
    const drops = document.querySelectorAll('.dropdown');
    drops.forEach(d => {
        d.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                // Check if clicking link or container
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

    // Clickable cards
    document.querySelectorAll('.feature-article').forEach(art => {
        art.addEventListener('click', (e) => {
            if (e.target.tagName !== 'A') {
                const link = art.querySelector('a.btn-soft');
                if (link) link.click();
            }
        });
    });
});

