def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("John", "Doe")
print()
display_name("Mr.", "John", "Doe")
print()

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              apt="100",
              city="detroit",
              state="MI",
              zip="12345")
print()


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "James", "Webb",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="12345")