document.addEventListener('DOMContentLoaded', function() {
    const days = document.querySelectorAll('.day');

    days.forEach(day => {
        day.addEventListener('mouseenter', function() {
            const tooltip = document.getElementById("tooltip");
            tooltip.innerHTML = `<b>Date:</b> ${day.dataset.date}<br><b>Duration</b> ${day.dataset.duration}`;
        });

        day.addEventListener('mouseleave', function() {
            const tooltip = document.getElementById("tooltip");
            tooltip.innerHTML = '';
        });
    });
});
