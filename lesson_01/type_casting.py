name = "Bro Coder"
age = 26
gpa = 4.8
is_student = True

print(type(name))
print(type(age))
print(type(gpa))

gpa = int(gpa)
print(gpa)

age = str(age)
print(age)

print(age, type(age))
age += "1"
print(age)

name = bool(name)
print(name) # True
user_input = ""
print(bool(user_input)) # False