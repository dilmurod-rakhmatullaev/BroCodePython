from car import Car


car1 = Car("Mercedes", 1999, "blue", True)
car2 = Car("BMW", 2000, "black", False)
car3 = Car("Tesla", 2025, "white", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.stop()
car3.describe()