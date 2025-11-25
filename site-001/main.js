// 網站主 JavaScript 檔案 (main.js)

document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    // 1. 漢堡選單切換 (Menu Toggle)
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            // 確保手機版下拉選單在主選單關閉時也隱藏
            if (!navLinks.classList.contains('active') && dropdownMenu) {
                dropdownMenu.classList.remove('active');
            }
        });
    }

    // 2. 下拉選單切換 (Dropdown Toggle) - 僅限手機版
    if (dropdownToggle && dropdownMenu) {
        dropdownToggle.addEventListener('click', (e) => {
            // 檢查是否為手機模式
            if (window.innerWidth <= 767) {
                e.preventDefault();
                dropdownMenu.classList.toggle('active');
            }
        });
    }

    // 3. 滾動固定導覽列 (Sticky Header Logic) - 確保樣式設定在 CSS 中
    // 這裡不需要額外的 JS 邏輯，因為 CSS 的 position: sticky 已經處理了

    // 4. 外部連結加上 rel="nofollow" 屬性
    document.querySelectorAll('a[href^="http"]:not([href*="' + window.location.hostname + '"])').forEach(externalLink => {
        if (!externalLink.hasAttribute('rel')) {
            externalLink.setAttribute('rel', 'nofollow noopener noreferrer');
        } else if (!externalLink.getAttribute('rel').includes('nofollow')) {
            externalLink.setAttribute('rel', externalLink.getAttribute('rel') + ' nofollow');
        }
    });
});