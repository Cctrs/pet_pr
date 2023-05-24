FILEPATH = "smartlist.txt"
FILEPATH_DONE = "done_task.txt"


def get_tasks(filepath=FILEPATH):
    with open(filepath, 'r') as tasks_local:
        tasks_local = tasks_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    with open(filepath, 'w') as doc:
        doc.writelines(tasks_arg)


def get_done_tasks(filepath=FILEPATH_DONE):
    with open(filepath, 'r') as done_local:
        done_local = done_local.readlines()
        return done_local


def write_done_tasks(tasks_done, filepath=FILEPATH_DONE):
    with open(filepath, 'w') as doc_done:
        doc_done.writelines(tasks_done)


def write_retro_tasks(tasks_arg, filepath):
    with open(filepath, 'w') as doc:
        doc.writelines(tasks_arg)


def read_retro_tasks(filepath=FILEPATH_DONE):
    with open(filepath, 'r') as done_local:
        done_local = done_local.readlines()
        return done_local