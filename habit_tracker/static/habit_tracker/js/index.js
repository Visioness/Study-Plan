document.addEventListener('DOMContentLoaded', function() {
    const days = document.querySelectorAll('.day');

    days.forEach(day => {
        day.addEventListener('mouseenter', function() {
            const tooltip = this.querySelector("#tooltip");
            tooltip.style.display = 'block';
        });

        day.addEventListener('mouseleave', function() {
            const tooltip = this.querySelector("#tooltip");
            tooltip.style.display = 'none';
        });
    });
});
