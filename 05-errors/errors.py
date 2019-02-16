class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"wrong car of {car}, use the Car object instead")
        self.cars.append(car)


ford = Garage()
new_car = Car("some make", "some model")
ford.add_car(new_car)
print(len(ford))
