import zipfile as zf
import pathlib as pb
import time as t


def compress_zip(src, dest):
    # Write the location to store the compressed files
    x = pb.Path(dest, "compressed" + t.strftime("%Y_%m_%d_%H_%M_%S")+'.zip')
    #print(x)

    # Loop Through the files and save it in the zip file created above
    with zf.ZipFile(x, "w") as file:
        for i in src:
            absolutename = pb.Path(i)
            #print(i)
            file.write(i, arcname=absolutename.name)



def un_zipper(src, dest):
    # Extract all files in a zip file
    with zf.ZipFile(src, "r") as file:
        file.extractall(dest)



if __name__ == '__main__':
    #compress_zip(src = ['Files to Compress'+'\\a.txt'], dest = 'Folder to Store Compress')
    un_zipper(r'C:\Users\suhas\PycharmProjects\PythonProject-App1\Folder to Store Compress\compressed2025_07_05_13_22_58.zip', r'C:\Users\suhas\PycharmProjects\PythonProject-App1\Folder to Store Uncompressed')

