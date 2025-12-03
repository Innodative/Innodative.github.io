// Dark mode toggle functionality
(function() {
    // Check for saved theme preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);

    // Wait for DOM to load
    document.addEventListener('DOMContentLoaded', function() {
        const toggleButton = document.getElementById('theme-toggle');
        
        if (toggleButton) {
            // Set initial button state
            updateButtonText(currentTheme);
            
            // Toggle theme on button click
            toggleButton.addEventListener('click', function() {
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                updateButtonText(newTheme);
            });
        }
    });

    function updateButtonText(theme) {
        const toggleButton = document.getElementById('theme-toggle');
        if (toggleButton) {
            toggleButton.textContent = theme === 'light' ? '🌙' : '☀️';
            toggleButton.setAttribute('aria-label', theme === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
        }
    }
})();
