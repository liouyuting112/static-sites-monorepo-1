document.addEventListener('DOMContentLoaded', () => {
    // Hamburger logic
    const burger = document.querySelector('.hamburger');
    const nav = document.querySelector('.nav-links');
    
    if (burger) {
        burger.addEventListener('click', () => {
            nav.classList.toggle('active');
            burger.textContent = nav.classList.contains('active') ? '✕' : '☰';
        });
    }

    // Dropdown for mobile
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(drop => {
        drop.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                // Prevent jumping if clicking the label
                if (e.target.getAttribute('href') === '#') {
                    e.preventDefault();
                }
                drop.classList.toggle('active');
            }
        });
    });

    // Date link logic
    const daily = document.getElementById('daily-link');
    if (daily) {
        daily.href = 'articles/2025-11-28.html';
    }

    // Card click
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('click', (e) => {
            if(e.target.tagName !== 'A') {
                const btn = card.querySelector('.read-btn');
                if(btn) btn.click();
            }
        });
    });
});

