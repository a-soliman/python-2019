from utils.database import Database

USER_CHOICE = """
Enter: 
- "a" to add a new book
- "l" to list all books
- "r" to mark book as read
- "d" to delete a book
- "g" to get a book by name
- "q" to quit
"""

db = Database("data.db")
db.create_book_table()


def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":

        if user_input == "l":
            books = db.list()
            print(books)

        if user_input == "a":
            name = input("Book Name: ").strip()
            author = input("Book Author's Name: ").strip()
            db.add(name, author)

        if user_input == "g":
            name = input("Book Name: ").strip()
            book = db.get(name)
            print(book)

        if user_input == "r":
            name = input("Book Name: ").strip()
            db.mark_read(name)

        if user_input == "d":
            name = input("Book Name: ").strip()
            db.delete(name)

        user_input = input(USER_CHOICE)


menu()
