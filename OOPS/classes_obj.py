class Student:
    # Constructor
    def __init__(self):
        self.name = input("Enter a name = ")
        self.age = int(input("Enter a age = "))
        self.gender = input("Enter a gender = ")

    def display(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")


s1 = Student()
s1.display()
