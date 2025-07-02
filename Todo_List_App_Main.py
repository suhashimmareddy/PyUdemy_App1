from idlelib import window

import Function_Todo_App as fta
import FreeSimpleGUI as fsg

label = fsg.Text("Type in the todo item:")
input_box = fsg.InputText(tooltip = 'Enter Todo')
add_button = fsg.Button("ADD")

Window = fsg.Window("Todos",
                    [[label],
                            [input_box,add_button]])
Window.read()
Window.close()
