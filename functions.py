FILEPATH = "smartlist.txt"


def get_tasks(filepath=FILEPATH):
    with open(filepath, 'r') as tasks_local:
        tasks_local = tasks_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    with open(filepath, 'w') as doc:
        doc.writelines(tasks_arg)