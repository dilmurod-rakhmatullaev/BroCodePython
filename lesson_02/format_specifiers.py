price1 = 3689.14159
price2 = -9874.65
price3 = 1297.34

print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3: .3f}")
print()
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")
print()
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:>010}")
print(f"Price 3 is ${price3:^010}")
print()
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3: }")
print()
print(f"Price 1 is ${price1:,.1f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.3f}")

"""
Price 1 is $3689.142
Price 2 is $-9874.650
Price 3 is $ 1297.340

Price 1 is $3689.14159
Price 2 is $  -9874.65
Price 3 is $   1297.34

Price 1 is $3689.14159
Price 2 is $00-9874.65
Price 3 is $01297.3400

Price 1 is $+3689.14159
Price 2 is $-9874.65
Price 3 is $ 1297.34

Price 1 is $3,689.1
Price 2 is $-9,874.65
Price 3 is $1,297.340
"""