class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def __str__(self):
        return f"Student {self.name}."

    def avrage(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5


dd = WorkingStudent("DD", "some School", 15.50)
print(dd.weekly_salary)
