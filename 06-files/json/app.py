import json

file = open("friends.json", "r")
file_content = json.load(file)
print(file_content)

cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Jeep", "model": "Compass"}
]

cars_dict = {
    "cars": cars
}

cars_file = open("cars.json", "w")
cars_file.write(json.dumps(cars_dict, indent=4))
