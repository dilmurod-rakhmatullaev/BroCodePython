word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter} in the secret word")
else:
    print(f"{letter} is not in the secret word")
print()

if letter not in word:
    print(f"No, {letter} is NOT in the secret word")
else:
    print(f"Yes, {letter} is there!")
print()

students = {"Sam", "John", "Lisa"}

student = input("Enter a student name: ")

if student in students:
    print(f"{student} is in the students list")
else:
    print(f"{student} was not found")
print()

if student not in students:
    print(f"Oops, {student} is not in the students list")
else:
    print(f"Yeah, {student} is there!")
print()


grades = {"Sandy": "A",
          "Bob": "B",
          "Joe": "C",
          "Alice": "D"}

student = input("Enter a student name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")