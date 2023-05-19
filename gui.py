import PySimpleGUI

text1 = PySimpleGUI.Text('Enter your note: ')
input_box = PySimpleGUI.InputText(tooltip='Enter note here')
button_example = PySimpleGUI.Button('Add note')
button_example2 = PySimpleGUI.Button('Edit note')

start_window = PySimpleGUI.Window('Notes', layout=[[text1, input_box],
                                                   [button_example],
                                                   [button_example2]])
start_window.read()
start_window.close()
