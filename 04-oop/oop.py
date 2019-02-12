class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avrage_grade(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __str__(self):
        string = ""
        for car in self.cars:
            string += car + " "
        return string

    def __getitem__(self, i):
        return self.cars[i]

    def park(self, model):
        self.cars.append(model)

# rolf = Student("Rolf", [70, 88, 90, 99])
# print(rolf.avrage_grade())


ford = Garage()
ford.park("Fiesta")

print(len(ford))
print(str(ford))
print(ford[0])
