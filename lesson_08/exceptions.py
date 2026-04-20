try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can not divide by zero!")
except ValueError:
    print("Please enter a number!")
except Exception as e:
    print(e)
    # print("Something went wrong!")
finally:
    print("Do some cleanup here")