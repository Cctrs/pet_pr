import PySimpleGUI

import functions

text1 = PySimpleGUI.Text('Enter your note: ')
input_box = PySimpleGUI.InputText(tooltip='Enter note here', key='note')
button_example = PySimpleGUI.Button('Add note')
button_example2 = PySimpleGUI.Button('Edit note')
notes_list = PySimpleGUI.Listbox(values=functions.get_notes(), key='notes_item',
                                 enable_events=True, size=(100, 20))

start_window = PySimpleGUI.Window('Notes',
                                  layout=[[text1, input_box, button_example],
                                          [notes_list], [button_example2]],
                                  font=('Ariel', 10))

while True:
    event, values = start_window.read()
    print(event)
    print(values)
    match event:
        case 'Add note':
            notes = functions.get_notes()
            new_note = values['note'] + '\n'
            notes.append(new_note)
            functions.write_notes(notes)
            start_window['notes_item'].update(values=notes)
            start_window['note'].update('')
        case 'Edit note':
            edit_note = values['notes_item'][0]
            new_note = values['note']
            notes = functions.get_notes()
            index = notes.index(edit_note)
            notes[index] = new_note + '\n'
            functions.write_notes(notes)
            start_window['notes_item'].update(values=notes)
        case 'notes_item':
            start_window['note'].update(value=values['notes_item'][0])
        case PySimpleGUI.WIN_CLOSED:
            break


start_window.close()
