class Student:
    def __init__(self, Name, Age):
        self.name = Name
        self.Age = Age
        self.School= "Sir Syed public"

    def display(self):
        print(f"Student name {self.name}\n"f"Student Age: {self.Age}\n" f"School: {self.School}")

student1 = Student("Sumair", 26)
student1.display()
print()

student2 = Student("Umair", 26)
student2.display()
print()
student3 = Student("mair", 26)
student3.display()
print()
