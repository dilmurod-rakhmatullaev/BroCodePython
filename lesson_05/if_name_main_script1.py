# from if_name_main_script2 import *

# print(dir())
# print(__name__)

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()

"""
This is script1
Your favorite food is pizza
Goodbye!
"""