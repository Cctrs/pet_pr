import PySimpleGUI

import functions

text1 = PySimpleGUI.Text('Enter your task: ')
input_box = PySimpleGUI.InputText(tooltip='Enter task here', key='note')
button_example = PySimpleGUI.Button('Add task')
button_example2 = PySimpleGUI.Button('Edit task')
tasks_list = PySimpleGUI.Listbox(values=functions.get_tasks(), key='tasks_item',
                                 enable_events=True, size=(100, 20))

start_window = PySimpleGUI.Window('Tasks',
                                  layout=[[text1, input_box, button_example],
                                          [tasks_list], [button_example2]],
                                  font=('Ariel', 10))

while True:
    event, values = start_window.read()
    print(event)
    print(values)
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
        case PySimpleGUI.WIN_CLOSED:
            break


start_window.close()
