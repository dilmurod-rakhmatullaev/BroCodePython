doubles1 = []
for x in range(1, 11):
    doubles1.append(x * 2)

print(doubles1)


doubles2 = [x ** 2 for x in range(1, 11)]
triples = [y ** 3 for y in range(1, 11)]
squares = [z ** 4 for z in range(1, 11)]

print(doubles2)
print(triples)
print(squares)


fruits = ["apple", "banana", "cherry", "orange"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


numbers = [1, -2, 3, -4, 5, -6, 7, 8, 9, -10]

positive_nums = [num for num in numbers if num > 0]
print(positive_nums)

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

odd_nums = [num for num in numbers if num % 2 != 0]     # if not num % 2 == 0
print(odd_nums)


grades = [84, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)