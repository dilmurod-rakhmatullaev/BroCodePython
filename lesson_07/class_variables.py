class Student:

    class_year = 2025
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("John", 20)
student2 = Student("Michael", 21)
student3 = Student("Bob", 22)
student4 = Student("David", 23)

print(student1.name)
print(student2.age)
print(student1.class_year)  # 2025
print(Student.class_year)   # 2025

print(f"My graduation class of {Student.class_year} has {Student.num_students} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)