// Animation-specific JavaScript

// Mobile nav category dropdowns (Social Media, SEO, Branding & Campaigns, Creatives,
// IT Solutions, About Us) - each is an independent accordion, one open at a time.
document.addEventListener('DOMContentLoaded', function() {
    const dropdownButtons = document.querySelectorAll('.mobile-dropdown-btn');

    dropdownButtons.forEach((btn) => {
        const panel = btn.nextElementSibling;
        const icon = btn.querySelector('.mobile-dropdown-icon');
        if (!panel) return;

        btn.addEventListener('click', () => {
            const isOpen = panel.classList.contains('max-h-96');

            // Close any other open accordion first
            dropdownButtons.forEach((otherBtn) => {
                if (otherBtn === btn) return;
                const otherPanel = otherBtn.nextElementSibling;
                const otherIcon = otherBtn.querySelector('.mobile-dropdown-icon');
                if (otherPanel && otherPanel.classList.contains('max-h-96')) {
                    otherPanel.classList.remove('max-h-96');
                    otherPanel.classList.add('max-h-0');
                    if (otherIcon) otherIcon.classList.remove('rotate-180');
                }
            });

            if (isOpen) {
                panel.classList.remove('max-h-96');
                panel.classList.add('max-h-0');
                if (icon) icon.classList.remove('rotate-180');
            } else {
                panel.classList.remove('max-h-0');
                panel.classList.add('max-h-96');
                if (icon) icon.classList.add('rotate-180');
            }
        });
    });

    // Video lazy loading
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        video.setAttribute('loading', 'lazy');
    });
    
    // Image lazy loading — skip images already marked as eager (e.g. the navbar logo)
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        if (img.getAttribute('loading') !== 'eager') {
            img.setAttribute('loading', 'lazy');
        }
    });
});