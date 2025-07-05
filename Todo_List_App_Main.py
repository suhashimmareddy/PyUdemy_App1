#from idlelib import window

import Function_Todo_App as fta
import FreeSimpleGUI as fsg
import time as t
import os

if not os.path.exists('Todos.txt'):
    with open('Todos.txt', 'w') as file:
        pass


fsg.theme('black')

#set-executionpolicy remoteassigned -scope currentuser -- this to use when terminal has no .venv

clock = fsg.Text('',key='CLOCK')
label = fsg.Text("Type in the todo item:")
input_box = fsg.InputText(tooltip = 'Enter Todo', key = 'INPUT')
add_button = fsg.Button("ADD", key = 'ADD')
# add_button = fsg.Button(size=2, image_source='name.png', mouseover_colors='LightBlue2', tooltip= 'Add Todo',  key = 'ADD')
edit_button = fsg.Button("EDIT", key = 'EDIT')
complete_button = fsg.Button("DONE", key = 'DONE')
exit_button = fsg.Button("CLOSE", key = 'CLOSE')
list_box = fsg.Listbox(values = fta.get_todos(), key = 'LIST_BOX', enable_events = True, size = [44,10])

Window = fsg.Window("Su's Todo Items",
                    [ [clock],
                            [label],
                            [input_box,add_button],
                            [list_box, edit_button],
                            [complete_button, exit_button]],
                    font = ('Helvetica', 12))

while True:

    event, values = Window.read(timeout=200)
    match event:
        case fsg.WIN_CLOSED:
            break

    Window['CLOCK'].update(value = t.strftime('%Y %m %d - %H:%M:%S'))


    match event:
        case 'ADD':
            #get existing list of todos and the new list
            todos = fta.get_todos()
            new_val = values['INPUT']+'\n'

            #append the new item and write it back to the list
            todos.append(new_val)
            fta.write_todos(todos)

            # update the window with new list
            Window['LIST_BOX'].update(values=todos)

        case 'EDIT':
            try:
                #get the todo selected and item to replace with
                todo_sel = values['LIST_BOX'][0]
                new_todo_item = values['INPUT']+'\n'

                #logic to update the list
                todos = fta.get_todos()
                idx = todos.index(todo_sel)
                todos[idx] = new_todo_item
                fta.write_todos(todos)

                #update the window with new list
                Window['LIST_BOX'].update(values=todos)
            except IndexError:
                fsg.popup('Select an Item First!!', font = ('Helvetica', 12))


        case 'DONE':
            try:
                #get the todo to be deleted
                todo_completed = values['LIST_BOX'][0]

                #logic to update the list
                todos = fta.get_todos()
                todos.remove(todo_completed)
                fta.write_todos(todos)

                #update the window with new list
                Window['LIST_BOX'].update(values=todos)
                Window['INPUT'].update(value= "")

            except IndexError:
                fsg.popup('Select an Item First!!', font=('Helvetica', 12))

        case 'LIST_BOX':
            #Update the input area with the selected todo item
            Window['INPUT'].update(value = values['LIST_BOX'][0])

        case 'CLOSE':
            break



Window.close()
