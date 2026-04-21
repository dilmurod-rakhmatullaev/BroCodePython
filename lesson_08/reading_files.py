from json import JSONDecodeError

file_path = r"C:\Users\SB\Desktop\test2\input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f" Error {e}")

print("-----------------------------")
import json

file_path = r"C:\Users\SB\Desktop\test2\input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File not found")
except JSONDecodeError:
    print("Invalid JSON format")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f" Error {e}")


print("-----------------------------")
import csv

file_path = r"C:\Users\SB\Desktop\test2\input.csv"

try:
    with open(file_path, "r") as file:
        content1 = csv.reader(file)
        for line in content1:
            print(line)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f" Error {e}")