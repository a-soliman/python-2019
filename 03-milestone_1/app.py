class Movie:
    def __init__(self, name, year, director):
        self.name = name
        self.year = year
        self.director = director

    def get_info(self):
        print(f"{self.name} a movie by {self.director}, on {self.year}")


class Cinema:
    def __init__(self):
        self.movies = []

    def get_all(self):
        return self.movies

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_by_name(self, name):
        for movie in self.movies:
            if movie.name.lower() is name.lower():
                return movie
        return "Not found"

    def get_by_year(self, year):
        for movie in self.movies:
            if int(movie.year) is int(year):
                return movie
        return "Not found"

    def get_by_director(self, director):
        for movie in self.movies:
            if movie.director.lower() is director.lower():
                return movie
        return "Not found"


cinema = Cinema()
instructions = "(1) to view all movies. \n(2) to add a movie."

while (True):
    print(instructions)
    choice = None

    while choice is not "1" and choice is not "2":
        choice = input("What would you like to do? ")

    if choice is "1":
        print(f"There are a total of {len(cinema.get_all())} movies.")
        for movie in cinema.movies:
            movie.get_info()

    if choice is "2":
        name = None
        director = None
        year = None

        while name is None:
            name = input("Enter Movie name: ")

        while director is None:
            director = input("Enter director name: ")

        while year is None:
            year = input("Movie's release year: ")

        new_movie = Movie(name, year, director)
        cinema.add_movie(new_movie)
