for counter in reversed(range(1, 11)):
    print(counter)
print("Happy New Year!")

for x in range(1, 11, 2):
    print(x)


credit_card = "1234-5678-9012-3456"

for i in credit_card:
    print(i)


for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)


for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)