class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"


# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []

#     def append(self, value):
#         self.marks.append(value)

#     def avrage(self):
#         return sum(self.marks) / len(self.marks)

#     @classmethod
#     def say_hi(cls):
#         return "Hi"


# rolf = Student("Rolf", "MIT")
# rolf.append(78)
# rolf.append(99)

# print(rolf.avrage())
# print(Student.say_hi())
