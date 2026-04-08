from src.task import Task
from src.task_queue import TaskQueue


def main() -> None:
    """
    Запускает демонстрацию работы очереди задач
    """
    queue = TaskQueue(
        [
            Task(id="T-1", description="Покормить гусей", priority=10, status="new"),
            Task(id="T-2", description="Собрать докерфайл", priority=5, status="progress"),
            Task(id="T-3", description="Проложить оптоволокно", priority=7, status="new"),
        ]
    )

    print("Все задачи:")
    for task in queue:
        print(task.id, task.status, task.priority)
    print()
    print("Готовые задачи:")
    for task in queue.ready_tasks_stream():
        print(task.id, task.description)

if __name__ == "__main__":
    main()
