num = -8
print("positive" if num > 0 else "negative")
result = "even" if num % 2 == 0 else "odd"
print(result)


a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)


age = 25
status = "Adult" if age >= 18 else "Child"
print(status)


temp = 26
weather = "hot" if temp > 22 else "cold"
print(weather)


user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(user_role)