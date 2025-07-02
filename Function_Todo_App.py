
FP = "Todos.txt"

#Add First Function Here
"""
The Goal of this get_todos function is to get the todos list from a file
"""
def get_todos(File_Path = FP):
    with open(File_Path, 'r') as f:
        todos_read = f.readlines()
    return todos_read


#Add Second Function Here
"""
The Goal of this write_todos function is to write the todos list from a file
"""
def write_todos(todos_list, File_Path = FP):
    with open(File_Path, 'w') as f:
        f.writelines(todos_list)

if __name__ == '__main__':
    x = get_todos()
    print(x)
    x.append('three'+'\n')
    write_todos(x)
    x = get_todos()
    print(x)