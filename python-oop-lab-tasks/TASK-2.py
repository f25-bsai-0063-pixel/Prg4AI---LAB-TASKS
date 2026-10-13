#Lab Task 2

class student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)


S1 = student("Haseeb", 20, "CS")
S1.display()
