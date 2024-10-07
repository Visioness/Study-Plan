document.addEventListener('DOMContentLoaded', function() {
    window.onload = function() {
        const scrollContainer = document.querySelector('.container');
        scrollContainer.scrollLeft = 0;
    };
    
    window.onresize = function() {
        const scrollContainer = document.querySelector('.container');
        scrollContainer.scrollLeft = 0;
    };    
    
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
