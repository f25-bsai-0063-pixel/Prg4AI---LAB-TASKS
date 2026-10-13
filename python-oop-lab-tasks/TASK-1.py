#Lab Task 1

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)


class Graduate(Student):
    def __init__(self, name, age, course, research_topic):
        super().__init__(name, age, course)
        self.research_topic = research_topic

    def displayy(self):
        super().display()
        print(self.research_topic)


st1 = Student("Junaid", 20, "P4AI")
st1.display()

st2 = Graduate("Muneeb", 20, "AI", "Artificial Intelligence")
st2.displayy()
