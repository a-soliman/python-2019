from utils import database


class Book:
    def __init__(self, name, author, read=False):
        self.name = name
        self.author = author
        self.read = read

    def __repr__(self):
        return (f"<Book {self.name} by {self.author} read: {self.read}>")

    def save(self):
        database.books.append(self)

    def update(self):
        for i in range(len(database.books)):
            book = database.books[i]
            if book.name == self.name:
                database.books[i] = self
                return True
        return False

    def delete(self):
        for i in range(len(database.books)):
            book = database.books[i]
            if book.name == self.name:
                return database.books.pop(i)
