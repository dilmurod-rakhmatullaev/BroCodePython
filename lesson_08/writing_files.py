txt_data = "I like pizza"

file_path1 = "output.txt"
file_path_2 = r"C:\Users\SB\Desktop\test2\test2.txt"

try:
    with open(file_path_2, "w") as file:
        file.write(txt_data + "\n")
        print(f"txt file '{file_path_2}' was created!")
except FileNotFoundError:
    print("File doesn't exist!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")


employees = ["Ashly", "Bob", "Cole", "David"]
file_path_3 = r"C:\Users\SB\Desktop\test2\test3.txt"
try:
    with open(file_path_3, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path_3}' was created!")
except FileNotFoundError:
    print("File doesn't exist!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")


import json

employee = {
    "name": "Ashly",
    "age": 20,
    "job": "Engineer",
}

file_output_4 = r"C:\Users\SB\Desktop\test2\test4.json"

try:
    with open (file_output_4, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_output_4}' was created!")
except FileNotFoundError:
    print("File doesn't exist!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")


import csv

employees = [["Name", "Age", "Job"],
             ["Ferguson", 30, "Manager"],
             ["George", 45, "Scientist"],
             ["Ive", 22, "Singer"]]

file_path_5 = r"C:\Users\SB\Desktop\test2\test5.csv"

try:
    with open(file_path_5, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path_5}' was created!")
except FileNotFoundError:
    print("File doesn't exist!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"Error: {e}")