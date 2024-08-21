document.addEventListener('DOMContentLoaded', function () {
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

                fetch("/tasks/update-task-position/", {
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
});