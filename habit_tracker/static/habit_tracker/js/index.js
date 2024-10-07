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

    document.querySelectorAll('.tooltip-button').forEach(button => {
        button.addEventListener('click', function () {
            const dayDiv = this.closest('.day');

            const habitName = dayDiv.getAttribute('data-name');
            const habitDate = dayDiv.getAttribute('data-date');
            const habitDuration = dayDiv.getAttribute('data-duration');

            if (this.id == 'edit-button') {
                console.log('Clicked Edit');
                const newDuration = prompt('Enter the new duration.');
                const element = dayDiv.querySelector('#text-duration');

                if (newDuration && Number.isInteger(parseInt(newDuration, 10))) {
                    fetch(`/track/${habitName}/`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getCSRFToken(),
                        },
                        body: JSON.stringify({
                            habitDuration: newDuration,
                            habitDate: habitDate,
                        })
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.json();  // Ensure it's returning valid JSON
                    })
                    .then(data => {
                        if (data.success) {
                            alert(data.message);  // Show success message
                        } else {
                            alert('Failed to update habit');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
                }

                console.log(`${element.innerHTML}`);

            } else if (this.id == 'remove-button') {
                console.log('Clicked Remove');
            }
        });
    });
});

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
