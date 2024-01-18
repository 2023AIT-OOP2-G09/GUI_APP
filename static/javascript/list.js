  // Function to create schedule items and append them to the container
  function renderScheduleItems(data) {
    const container = document.getElementById('scheduleContainer');

    data.forEach(item => {
      const scheduleItem = document.createElement('div');
      scheduleItem.classList.add('schedule-item');
      scheduleItem.innerHTML = `<strong>Date:</strong> ${item.date}<br><strong>Time:</strong> ${item.time}<br><strong>Schedule:</strong> ${item.schedule}`;
      container.appendChild(scheduleItem);
    });
  }

  // Render schedule items on page load
  window.addEventListener('load', function () {
    renderScheduleItems(jsonData);
  });
  