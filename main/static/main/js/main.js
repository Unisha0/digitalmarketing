// Main JavaScript - Common functionality for all pages

// Initialize AOS
AOS.init({
    duration: 600,
    easing: 'ease-out-cubic',
    offset: 40,
    once: true,
    disable: window.matchMedia('(prefers-reduced-motion: reduce)').matches
});

// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        const setMenu = (open) => {
            mobileMenu.classList.toggle('open', open);
            document.body.classList.toggle('menu-open', open);
            mobileMenuButton.setAttribute('aria-expanded', String(open));
            mobileMenuButton.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        };
        mobileMenuButton.addEventListener('click', () => setMenu(!mobileMenu.classList.contains('open')));
        // close on link tap, backdrop tap, Escape, or when growing to desktop width
        mobileMenu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
        const backdrop = document.querySelector('.mobile-menu-backdrop');
        if (backdrop) backdrop.addEventListener('click', () => setMenu(false));
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
        window.matchMedia('(min-width: 1024px)').addEventListener('change', (e) => { if (e.matches) setMenu(false); });
    }
    
    // Navbar scroll effect
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');
    const scrollThreshold = 50;
    
    if (navbar) {
        navbar.classList.add('transition-transform', 'transition-opacity', 'duration-500', 'ease-in-out', 'opacity-100');

        const updateScrolledState = () => {
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
            navbar.classList.toggle('scrolled', currentScroll > 20);
        };
        updateScrolledState();

        window.addEventListener('scroll', () => {
            updateScrolledState();
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

            if (currentScroll - lastScroll > scrollThreshold && currentScroll > 100) {
                // scrolling down
                navbar.classList.add('-translate-y-full', 'opacity-0');
            } else if (lastScroll - currentScroll > scrollThreshold || currentScroll <= 100) {
                // scrolling up
                navbar.classList.remove('-translate-y-full', 'opacity-0');
                navbar.classList.add('opacity-100');
            }
            
            lastScroll = currentScroll <= 0 ? 0 : currentScroll;
        });
    }
    
    // Prevent horizontal overflow
    // (sideways overflow is clipped on <html> in CSS; body must not become a scroll container)
    
    // Check for any elements causing horizontal overflow
    function checkOverflow() {
        const bodyWidth = document.body.offsetWidth;
        const windowWidth = window.innerWidth;
        
        if (bodyWidth > windowWidth) {
            console.log('Horizontal overflow detected');
            // Force body to window width
        }
    }
    
    // Check on load and resize
    checkOverflow();
    window.addEventListener('resize', checkOverflow);
    
    // Desktop Services dropdown: position dropdown outside any stacking contexts
    // This moves the dropdown visually using fixed positioning so it appears above overlays
    function initDesktopDropdowns() {
        const groups = document.querySelectorAll('.relative.group');
        groups.forEach(group => {
            const dropdown = group.querySelector('.desktop-services-menu');
            const trigger = group.querySelector('a');
            if (!dropdown || !trigger) return;

            // Make sure dropdown is hidden by default; JS will handle visibility
            dropdown.style.display = 'none';

            let isVisible = false;

            function positionDropdown() {
                const rect = trigger.getBoundingClientRect();
                // position fixed so it's outside parent stacking contexts
                dropdown.style.position = 'fixed';
                dropdown.style.left = Math.max(8, rect.left) + 'px';
                dropdown.style.top = (rect.bottom + 6) + 'px';
                // ensure dropdown is at least as wide as trigger or w-48 (192px)
                const minW = Math.max(rect.width, 192);
                dropdown.style.minWidth = minW + 'px';
                dropdown.style.zIndex = '100000';
            }

            function showDropdown() {
                if (window.innerWidth < 768) return; // only desktop
                positionDropdown();
                dropdown.style.display = 'block';
                isVisible = true;
            }

            function hideDropdown() {
                dropdown.style.display = 'none';
                isVisible = false;
            }

            group.addEventListener('mouseenter', showDropdown);
            group.addEventListener('mouseleave', hideDropdown);
            window.addEventListener('resize', () => { if (isVisible) positionDropdown(); });
        });
    }

    initDesktopDropdowns();
});