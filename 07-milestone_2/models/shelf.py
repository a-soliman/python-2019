from utils import database
from .book import Book


class Shelf:
    def __init__(self):
        pass

    def __len__(self):
        return len(database.books)

    @classmethod
    def list_books(cls):
        return database.books

    def add_book(self, name, author):
        book = Book(name, author)
        book.save()
        return True

    def mark_book_read(self, name):
        for book in database.books:
            if book.name == name:
                book.read = True
                book.update()
                return True

    def delete_book(self, name):
        for book in database.books:
            if book.name == name:
                book.delete()
                return True
