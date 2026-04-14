def happy_birthday(name, age):
    print(f"Happy birthday, {name}!")
    print(f"You are {age} years old")

happy_birthday("Bro", 20)
happy_birthday("Steve", 35)
happy_birthday("Joe", 16)
print()

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due to {due_date}")

display_invoice("Bro", 20, "2020")
display_invoice("Sam", 10.57, "03/2020")
print()


def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiple(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiple(1, 2))
print(divide(1, 2))
print()


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

full_name = create_name("joe", "brown")

print(full_name)

