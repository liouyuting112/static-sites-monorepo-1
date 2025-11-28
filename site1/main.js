/**
 * Main JS for Site 1
 * Handles mobile navigation and dynamic date links.
 * Human note: Trying to keep this simple and robust!
 */

document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // Toggle hamburger icon animation if we had one, but simple is good.
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navLinks.contains(e.target) && !menuToggle.contains(e.target) && navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
            }
        });
    }

    // Dropdown interaction for mobile (click to expand)
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(drop => {
        drop.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                // Prevent immediate navigation if it's a parent link
                // But our structure usually has the parent as text or '#'
                const content = drop.querySelector('.dropdown-content');
                if (content) {
                    // Simple toggle for mobile display style
                    const currentDisplay = window.getComputedStyle(content).display;
                    content.style.display = (currentDisplay === 'none') ? 'flex' : 'none';
                }
            }
        });
    });

    // Daily Article Link Logic
    // We want the 'Daily Featured' link to point to today's article if it exists,
    // or a default fallback. For this static demo, we target '2025-11-28.html'.
    const dailyLink = document.getElementById('daily-featured-link');
    if (dailyLink) {
        // In a real dynamic site, we'd do:
        // const today = new Date().toISOString().split('T')[0];
        // dailyLink.href = `articles/${today}.html`;
        
        // For this demo, we hardcode to the one we generated:
        dailyLink.href = 'articles/2025-11-28.html';
        
        // Human note: Just in case the user changes the date on their PC, 
        // strictly speaking this should match the generated file name.
    }

    // Clickable Cards Logic
    const cards = document.querySelectorAll('.article-card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            const link = this.querySelector('a');
            if (link) {
                window.location.href = link.href;
            }
        });
    });
});
