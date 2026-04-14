import random

low = 1
high = 100
number = random.randint(low, high)
print(number)

floating_number = random.random()
print(floating_number)


options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

"""
55
0.5336469901424098
paper
['3', 'A', 'K', '9', 'Q', '2', '6', '5', 'J', '10', '7', '4', '8']
"""