import PySimpleGUI

text1 = PySimpleGUI.Text('Enter feet: ')
input_box = PySimpleGUI.InputText(tooltip='Enter feet here')

text2 = PySimpleGUI.Text('Enter inches: ')
input_box2 = PySimpleGUI.InputText(tooltip='Enter inches here')
button_example = PySimpleGUI.Button('Convert')
button_example2 = PySimpleGUI.Button('Convert2')

start_window = PySimpleGUI.Window('Convertor', layout=[[text1, input_box],
                                                       [text2, input_box2],
                                                       [button_example],
                                                       [button_example2]
                                                       ])
start_window.read()
start_window.close()
