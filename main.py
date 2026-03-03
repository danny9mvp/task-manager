from model.task import Task


task_list = [Task(1,
                  "Do my maths homework",
                  "Solve some 2nd grade equations",
                  "done"),
             Task(2,
                  "Solve the tech test",
                  "Submit the solution for the Python + SQL challenge for TCS",
                  "pending")
             ]


def get_latest_id():
    return max(list(map(lambda task: task.id, task_list)))


def get_task_by_id(task_id):
    return next(filter(lambda task: task.id == task_id, task_list), None)


def get_tasks_by_status(status):
    return list(filter(lambda task: task.status == status, task_list))


def add_task(task_id, title, description, status="pending"):
    task_list.append(Task(task_id, title, description, status))


def delete_task(task):
    task_list.remove(task)


def print_task_list(tasks):
    for task in tasks:
        print(task)


if "__main__":
    prompt = """
    What do you want to do?

    Press:
        'g' to get a task by id
        'l' to list all tasks 
        'lp' to list pending tasks 
        'a' to add a new task
        'u' to mark a task as done
        'd' to delete a task
    or type 'exit' to close the program
    """

    option = input(prompt)

    while option != 'exit':
        latest_id = get_latest_id()

        if option == "g":
            task_id = int(input("\tType the id of the task that you want to show: "))
            task = get_task_by_id(task_id)

            if task is None:
                print(f"\tTask with id {task_id} not found")
            else:
                print(task)

        if option == "l":
            print_task_list(task_list)

        if option == "lp":
            pending_tasks = get_tasks_by_status("pending")
            print_task_list(pending_tasks)

        if option == "a":
            task_id = latest_id + 1
            title_in = input("\tTitle: ")
            description_in = input("\tDescription: ")
            add_task(task_id, title_in, description_in)

        if option == "u":
            task_id = int(input("\tType the id of the task that you want to mark as done: "))
            task_to_update = get_task_by_id(task_id)

            if task_to_update is None:
                print(f"\tTask with id {task_id} not found")
            elif task_to_update.status == "pending":
                delete_task(task_to_update)
                task_to_update.status = "done"
                task_list.append(task_to_update)
                print(f"\tTask with id {task_id} marked as done")
                print(task_to_update)
            else:
                print(f"\tTask with id {task_id} is alreade done")

        if option == "d":
            task_id = int(input("\tType the id of the task that you want to delete: "))
            task_to_delete = get_task_by_id(task_id)

            if task_to_delete is None:
                print(f"\tTask with id {task_id} not found")
            else:
                delete_task(task_to_delete)
                print(f"\tTask with id {task_id} deleted")

        option = input(prompt)

