document.addEventListener('DOMContentLoaded', () => {
    const categoryButtons = document.querySelectorAll('.category-btn');
    const menuItems = document.querySelectorAll('.menu-item');

    // Function to filter menu items
    function filterMenuItems(category) {
        menuItems.forEach(item => {
            if (category === 'all' || item.dataset.category === category) {
                item.style.display = 'block';
                // Add animation delay based on item position
                const delay = Array.from(menuItems).indexOf(item) * 0.1;
                item.style.animationDelay = `${delay}s`;
            } else {
                item.style.display = 'none';
            }
        });
    }

    // Add click event listeners to category buttons
    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            categoryButtons.forEach(btn => btn.classList.remove('active'));
            // Add active class to clicked button
            button.classList.add('active');
            // Filter menu items
            filterMenuItems(button.dataset.category);
        });
    });

    // Add intersection observer for menu items
    const observerOptions = {
        threshold: 0.2
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe each menu item
    menuItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'all 0.5s ease-out';
        observer.observe(item);
    });

    // Initialize menu with all items visible
    filterMenuItems('all');
}); 