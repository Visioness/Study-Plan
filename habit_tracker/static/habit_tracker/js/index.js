document.addEventListener('DOMContentLoaded', function() {
    const days = document.querySelectorAll('.day');

    days.forEach(day => {
        day.addEventListener('mouseenter', function() {
            console.log('Hovering over day'); // Debugging statement
            const tooltip = this.querySelector(".tooltip");
            if (tooltip) {
                tooltip.style.display = 'block';
                console.log('Tooltip shown'); // Debugging statement
            } else {
                console.log('Tooltip not found'); // Debugging statement
            }
        });

        day.addEventListener('mouseleave', function() {
            const tooltip = this.querySelector(".tooltip");
            if (tooltip) {
                tooltip.style.display = 'none';
                console.log('Tooltip hidden'); // Debugging statement
            }
        });
    });
});
