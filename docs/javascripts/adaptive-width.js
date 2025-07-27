document.addEventListener("DOMContentLoaded", function() {
    adaptContentWidth();
});

function adaptContentWidth() {
    // Only apply on desktop screens
    if (window.innerWidth >= 1220) { // 76.25em = 1220px
        const rightSidebar = document.querySelector('.md-sidebar--secondary');
        const content = document.querySelector('.md-content');
        
        if (rightSidebar && content) {
            // Check if right sidebar has meaningful content
            const navList = rightSidebar.querySelector('.md-nav__list');
            const hasContent = navList && navList.children.length > 0;
            
            if (!hasContent) {
                // No TOC content - completely remove the sidebar element
                rightSidebar.remove();
                // Use full width
                content.style.marginLeft = '12rem';
                content.style.marginRight = '1rem';
                content.style.width = 'calc(100% - 13rem)';
            } else {
                // Has TOC content - ensure sidebar is visible
                content.style.marginLeft = '12rem';
                content.style.marginRight = '12rem';
                content.style.width = 'calc(100% - 24rem)';
            }
        } else if (!rightSidebar && content) {
            // Sidebar already removed - use full width
            content.style.marginLeft = '12rem';
            content.style.marginRight = '1rem';
            content.style.width = 'calc(100% - 13rem)';
        }
    }
}

// Re-check on page navigation
if (typeof document$ !== 'undefined') {
    document$.subscribe(() => {
        // Small delay to ensure DOM is ready
        setTimeout(adaptContentWidth, 100);
    });
}

// Re-check on window resize
window.addEventListener('resize', function() {
    setTimeout(adaptContentWidth, 100);
});