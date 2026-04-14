def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Welcome", "Ms.", "Dua", "Lipa")
hello("Hello", title = "Mr.", first = "Tom", last = "Tailor")
hello("Welcome", last = "Bieber", title = "Mr.", first = "Justin")
hello("Hi", "Ms.", first = "Camila", last = "Cabello")


for x in range(1, 11):
    print(x)

for x in range(1, 11):
    print(x, end=" ")   # end=" " - keyword argument
print()
print("1", "2", "3", "4", "5", sep="-")     # sep="-" - keyword argument

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)

