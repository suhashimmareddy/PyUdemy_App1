from idlelib import window

import FreeSimpleGUI as fsg

Files_Browse_label = fsg.Text("Select Files To Compress:")
Files_Browse_Input = fsg.Input()
Files_Browse_button = fsg.FileBrowse("Choose")

Folder_Compress_label = fsg.Text("Select Folder To Store Zip File:")
Folder_Compress_Input = fsg.Input()
Folder_Compress_button = fsg.FolderBrowse("Choose")

Compress_Button = fsg.Button("Compress")

Window = fsg.Window("File Compressor",
                    [[Files_Browse_label],
                            [Files_Browse_Input, Files_Browse_button],
                            [Folder_Compress_label],
                            [Folder_Compress_Input, Folder_Compress_button],
                            [Compress_Button]])
Window.read()
Window.close()
