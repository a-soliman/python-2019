from models.book import Book
from models.shelf import Shelf

USER_CHOICE = """
Enter: 
- "a" to add a new book
- "l" to list all books
- "r" to mark book as read
- "d" to delete a book
- "q" to quit
"""

shelv = Shelf()


def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":

        if user_input == "l":
            print(shelv.list_books())

        if user_input == "a":
            name = input("Book Name: ").strip()
            author = input("Book Author's Name: ").strip()

            if shelv.add_book(name, author):
                print(f"Added {name} by {author} successfully!")

        if user_input == "r":
            name = input("Book Name: ").strip()
            if shelv.mark_book_read(name):
                print(f"Updated {name}")

        if user_input == "d":
            name = input("Book Name: ").strip()
            if shelv.delete_book(name):
                print(f"Deleted {name} successfully.")

        user_input = input(USER_CHOICE)


menu()
