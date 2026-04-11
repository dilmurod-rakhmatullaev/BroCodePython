num1 = float(input("Enter the first number: "))
operator = input("Please enter an operator (+ - * /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Please enter one of these symbols: (+ - * /)")

print(f"The result is: {round(result, 3)}")