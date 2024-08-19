document.addEventListener('DOMContentLoaded', function () {
    let taskList = document.getElementById('task-list');

    if (taskList) {
        new Sortable(taskList, {
            animation: 150,
            onEnd: function (evt) {
                let taskIds = [];
                document.querySelectorAll('.task-item').forEach(function (item) {
                    taskIds.push(item.getAttribute('data-id'));
                });

                fetch("{% url 'update_task_position' %}", {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({ 'task_ids[]': taskIds })
                }).then(response => response.json())
                  .then(data => console.log(data))
                  .catch(error => console.error('Error:', error));
            }
        });
    }
});
