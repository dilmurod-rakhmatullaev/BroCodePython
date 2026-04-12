fruits = ["apple", "banana", "cherry", "coconut"]
vegetables = ["carrots", "potatoes", "tomato"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]


print(groceries[0][0])  # apple
print(groceries[1][2])  # tomato

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()