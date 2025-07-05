#from idlelib import window

import FreeSimpleGUI as fsg
from Function_To_Compress import compress_zip

fsg.theme('black')

Files_Browse_label = fsg.Text("Select Files To Compress:")
Files_Browse_Input = fsg.Input()
Files_Browse_button = fsg.FilesBrowse("Choose", key = "Files_Browse")

Folder_Compress_label = fsg.Text("Select Folder To Store Zip File:")
Folder_Compress_Input = fsg.Input()
Folder_Compress_button = fsg.FolderBrowse("Choose", key = "Folder_Compress")

Compress_Button = fsg.Button("Compress", key = "Compress")
output_label = fsg.Text(key= 'Output_Text', text_color='green')

Window = fsg.Window("File Compressor",
                    [[Files_Browse_label],
                            [Files_Browse_Input, Files_Browse_button],
                            [Folder_Compress_label],
                            [Folder_Compress_Input, Folder_Compress_button],
                            [Compress_Button, output_label]])
while True:
    event, values = Window.read()
    match event:
        case fsg.WIN_CLOSED:
            break

    #print(event)
    #print(values)
    filepaths = values["Files_Browse"].split(";")
    folderpath = values["Folder_Compress"]
    compress_zip(filepaths, folderpath)
    Window["Output_Text"].update(value = "Files are now Compressed")


Window.close()
