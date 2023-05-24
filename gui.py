import time

import PySimpleGUI

import functions

PySimpleGUI.theme("DarkGreen3")

text1 = PySimpleGUI.Text('Enter your task: ')
input_box = PySimpleGUI.InputText(tooltip='Enter task here', key='task')
button_add = PySimpleGUI.Button('Add task', mouseover_colors="Green", key='Add')
button_edit = PySimpleGUI.Button('Edit task', mouseover_colors="Green", key='Edit')
button_done = PySimpleGUI.Button('Done!', mouseover_colors="Green", key='Done')
button_exit = PySimpleGUI.Button('Exit', mouseover_colors="Green", key='Exit')
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
        case 'Add':
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            start_window['tasks_item'].update(values=tasks)
            start_window['task'].update('')
        case 'Edit':
            try:
                edit_task = values['tasks_item'][0]
                new_task = values['task']
                tasks = functions.get_tasks()
                index = tasks.index(edit_task)
                tasks[index] = new_task + '\n'
                functions.write_tasks(tasks)
                start_window['tasks_item'].update(values=tasks)
            except IndexError:
                PySimpleGUI.Popup('Please, select the task to edit.', title="Edit Window")
        case 'tasks_item':
            start_window['task'].update(value=values['tasks_item'][0])
        case 'Done':
            try:
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
            except IndexError:
                PySimpleGUI.Popup('Please, select the completed task.', title='Complete Window')
        case 'Exit':
            break
        case PySimpleGUI.WIN_CLOSED:
            break


start_window.close()
