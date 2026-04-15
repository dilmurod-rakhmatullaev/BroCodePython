numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for rev_num in reversed(numbers):
    print(rev_num, end=" ")
print()

fruits = {"apple", "banana", "cherry", "orange"}

for fruit in fruits:
    print(fruit)
# But 'set' object is not reversible!

name = "Bro Code"

for character in name:
    print(character, end="")
print()

my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4}

for key in my_dictionary:
    print(key, end=" ")
print()

for value in my_dictionary.values():
    print(value, end=" ")
print()

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
print()