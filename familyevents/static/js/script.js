// script.js
document.addEventListener('DOMContentLoaded', function() {
    const clickElement = document.getElementById('menu-icon');
        const targetElement = document.getElementById('nav-bar-small');

        clickElement.addEventListener('click', function() {
            // Add the new class to the target element
            targetElement.classList.toggle('nav-bar-small-show');
        });
});
