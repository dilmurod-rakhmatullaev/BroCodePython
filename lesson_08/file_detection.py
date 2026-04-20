import os

file_path1 = "test1.txt"
file_path2 = "C:\\Users\\User\\Desktop\\test2"
file_path3 = "C:/Users/User/Desktop/test3.txt"

path_files = [file_path1, file_path2, file_path3]
for file_path in path_files:
    if os.path.exists(file_path):
        print("Path and/or file exists!")

        if os.path.isfile(file_path):
            print("File exists!")
        elif os.path.isdir(file_path):
            print("Directory exists!")
    else:
        print("Path or file does not exist!")
    print()