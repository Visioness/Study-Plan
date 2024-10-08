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
            const habitDate = dayDiv.getAttribute('data-date');
            
            const durationElement = dayDiv.querySelector('#text-duration');

            if (this.id == 'edit-button') {
                let newDuration = prompt('Enter the new duration.');
                newDuration = parseInt(newDuration, 10);
                if (isNaN(newDuration) || newDuration < 0) {
                    alert('Please enter a valid non-negative integer for duration.');
                    return;
                }
                
                fetch(url, {
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
                        durationElement.textContent = newDuration;
                        updateIntensities(data.entries);

                    } else {
                        alert('Failed to update habit');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });

            } else if (this.id == 'remove-button') {
                fetch(url, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken(),
                    },
                    body: JSON.stringify({
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
                        durationElement.textContent = 0;
                        updateIntensities(data.entries);

                    } else {
                        alert('Failed to update habit');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        });
    });
});

// Function to update intensities for all habit entries
function updateIntensities(entries) {
    entries.forEach(entry => {
        const dayDiv = document.querySelector(`.day[data-date="${entry.date}"]`);
        if (dayDiv) {
            const dayInner = dayDiv.querySelector('.day-inner');
            dayInner.style.backgroundColor = `rgba(240, 94, 155, ${entry.intensity})`;
        }
    });
}

function getCSRFToken() {
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            csrfToken = decodeURIComponent(cookie.substring('csrftoken='.length));
            break;
        }
    }
    return csrfToken;
}