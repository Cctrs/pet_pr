import time

import PySimpleGUI

import functions

text1 = PySimpleGUI.Text('Enter your task: ')
input_box = PySimpleGUI.InputText(tooltip='Enter task here', key='task')
button_add = PySimpleGUI.Button('Add task')
button_edit = PySimpleGUI.Button('Edit task')
button_done = PySimpleGUI.Button('Done!')
button_exit = PySimpleGUI.Button('Exit')
tasks_list = PySimpleGUI.Listbox(values=functions.get_tasks(), key='tasks_item',
                                 enable_events=True, size=(100, 20))

start_window = PySimpleGUI.Window('Tasks',
                                  layout=[[text1, input_box, button_add],
                                          [tasks_list], [button_edit],
                                          [button_done],
                                          [button_exit]],
                                  font=('Ariel', 10))

while True:
    event, values = start_window.read()
    match event:
        case 'Add task':
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            start_window['tasks_item'].update(values=tasks)
            start_window['task'].update('')
        case 'Edit task':
            edit_task = values['tasks_item'][0]
            new_task = values['task']
            tasks = functions.get_tasks()
            index = tasks.index(edit_task)
            tasks[index] = new_task + '\n'
            functions.write_tasks(tasks)
            start_window['tasks_item'].update(values=tasks)
        case 'tasks_item':
            start_window['task'].update(value=values['tasks_item'][0])
        case 'Done!':
            task_done = values['tasks_item'][0]
            done_tasks_doc = functions.get_done_tasks()
            date_done = time.strftime("%Y-%B-%d %H:%M")
            done_tasks_doc.append(task_done + date_done + '\n')
            functions.write_done_tasks(done_tasks_doc)
            tasks = functions.get_tasks()
            tasks.remove(task_done)
            functions.write_tasks(tasks)
            start_window['tasks_item'].update(values=tasks)
            start_window['task'].update('')
        case 'Exit':
            break
        case PySimpleGUI.WIN_CLOSED:
            break


start_window.close()
