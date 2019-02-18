'''
Concerned with storing and retriving from a list.
'''
from .database_connection import DatabaseConnection


class Database:
    def __init__(self, datafile):
        self.data = datafile

    def create_book_table(self):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)")

    def list(self):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM books")
            return [{"name": row[0], "author": row[1], "read": row[2]}
                    for row in cursor.fetchall()]

    def add(self, name, author):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO books VALUES(? ,? , 0)", (name, author))

    def mark_read(self, name):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))

    def get(self, name):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM books WHERE name=?", (name,))
            res = cursor.fetchone()
            return {"name": res[0], "author": res[1], "read": res[2]}

    def delete(self, name):
        with DatabaseConnection(self.data) as connection:
            cursor = connection.cursor()

            cursor.execute("DELETE FROM books WHERE name=?", (name,))
