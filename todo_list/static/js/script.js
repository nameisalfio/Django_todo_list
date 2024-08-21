document.addEventListener('DOMContentLoaded', function () {

    // Handle drag-and-drop reordering of tasks
    const taskList = document.getElementById('task-list');
    if (taskList) {
        new Sortable(taskList, {
            animation: 150,
            handle: '.task-card',
            onStart: function (evt) {
                evt.item.classList.add('dragging');
            },
            onEnd: function (evt) {
                evt.item.classList.remove('dragging');
                let taskIds = [];
                document.querySelectorAll('.task-item').forEach(function (item) {
                    taskIds.push(item.getAttribute('data-id'));
                });

                fetch("/update-task-position/", {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ task_ids: taskIds })
                })
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
            }
        });
    }

    // Handle status toggling of tasks
    document.querySelectorAll('.status-btn').forEach(function (button) {
        button.addEventListener('click', function () {
            const taskId = this.getAttribute('data-id');
            fetch(`/toggle-task-status/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log('Response data:', data); // Debugging log
                if (data.status === 'success') {
                    // Toggle the status in the UI
                    const isCompleted = this.classList.contains('completed');
                    this.classList.toggle('completed', !isCompleted);
                    this.classList.toggle('not-completed', isCompleted);
                    this.title = !isCompleted ? 'Completed' : 'Not Completed';

                    // Update the SVG path
                    const path = this.querySelector('path');
                    if (path) {
                        path.remove();
                    }
                    if (!isCompleted) {
                        const newPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                        newPath.setAttribute('d', 'M7 12l4 4 6-6');
                        newPath.setAttribute('stroke', 'green');
                        newPath.setAttribute('stroke-width', '3');
                        newPath.setAttribute('fill', 'none');
                        this.querySelector('svg').appendChild(newPath);
                    }
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

});
