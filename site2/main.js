/**
 * Site 2 JS - Focus on clean interactions
 */
document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu
    const menuBtn = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-links');
    
    if (menuBtn && nav) {
        menuBtn.addEventListener('click', () => {
            nav.classList.toggle('active');
            // Change icon if needed, currently text or css icon
        });
    }

    // Mobile Dropdown Handling
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(drop => {
        const link = drop.querySelector('a'); // The main link
        link.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.preventDefault(); // Stop jump
                drop.classList.toggle('active');
                
                // Toggle display of content
                const content = drop.querySelector('.dropdown-content');
                if (content) {
                    content.style.display = content.style.display === 'block' ? 'none' : 'block';
                }
            }
        });
    });

    // Date Logic for Daily Article
    const dailyLink = document.getElementById('daily-link');
    if (dailyLink) {
        // Hardcoded for demo consistency
        dailyLink.href = 'articles/2025-11-28.html';
    }

    // Feature Card Whole-Click
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach(card => {
        card.addEventListener('click', (e) => {
            // Avoid double click if clicking the actual link
            if (e.target.tagName !== 'A') {
                const link = card.querySelector('a.read-more-btn');
                if (link) link.click();
            }
        });
    });
});

