fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[::-1])

# print(help(fruits))
# print(dir(fruits))

print(len(fruits))

print("apple" in fruits)    # True
fruits.append("pear")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
# fruits.clear()
print(fruits.index("banana"))
print(fruits.count("pineapple"))


fruits[1] = "pineapple"
for fruit in fruits:
    print(fruit)


laptops = {"Macbook", "Acer", "HP", "MSI"}
print(laptops)
laptops.add("ASUS")
laptops.remove("Acer")
laptops.pop()
print(laptops)


animals = ("lion", "tiger", "wolf", "fox")
print(animals)
print("dog" in animals)
print(animals.count("tiger"))

for animal in animals:
    print(animal)