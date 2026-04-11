name = input("Enter your full name: ")

result1 = len(name)
result2 = name.find("R")
result3 = name.rfind("t")
result4 = name.capitalize()
result5 = name.upper()
result6 = name.lower()
result7 = name.isdigit()
result8 = name.isalpha()

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)

phone_number = input("Enter your phone number: ")
result9 = phone_number.count("-")
print(result9)

result10 = phone_number.replace("-", "")
print(result10)


username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can not be longer than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can not contain spaces")
elif not username.isalpha():
    print("Your username should contain a-z characters")
else:
    print(f"Welcome {username}")
