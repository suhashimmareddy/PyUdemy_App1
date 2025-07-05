#from idlelib import window

import FreeSimpleGUI as fsg
from Function_To_Compress import un_zipper

fsg.theme('black')

File_Browse_label = fsg.Text("Select Files To Un-Zip:")
File_Browse_Input = fsg.Input()
File_Browse_button = fsg.FileBrowse("Choose", key = "File_Browse")

Folder_DeCompress_label = fsg.Text("Select Folder To Store Un-Zipped Files:")
Folder_DeCompress_Input = fsg.Input()
Folder_DeCompress_button = fsg.FolderBrowse("Choose", key = "Folder_DeCompress")

Extract_Button = fsg.Button("Un-Zip", key = "Un-Zip")
output_label_De = fsg.Text(key= 'Output_Text', text_color='green')

Window = fsg.Window("File Un-Zipper",
                    [[File_Browse_label],
                            [File_Browse_Input, File_Browse_button],
                            [Folder_DeCompress_label],
                            [Folder_DeCompress_Input, Folder_DeCompress_button],
                            [Extract_Button, output_label_De]])
while True:
    event, values = Window.read()
    match event:
        case fsg.WIN_CLOSED:
            break

    #print(event)
    #print(values)
    File1 = values["File_Browse"]
    folder1 = values["Folder_DeCompress"]
    un_zipper(File1, folder1)
    Window["Output_Text"].update(value = "Files are now Un-Zipped")

Window.close()
