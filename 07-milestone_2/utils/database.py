'''
Concerned with storing and retriving from a list.
'''
import sqlite3


class Database:
    def __init__(self, datafile):
        self.data = datafile

    def create_book_table(self):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS books (name text primary key, author text, read integer)")

        connection.commit()
        connection.close()

    def list(self):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")
        books = [{"name": row[0], "author": row[1], "read": row[2]}
                 for row in cursor.fetchall()]

        connection.close()
        return books

    def add(self, name, author):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute("INSERT INTO books VALUES(? ,? , 0)", (name, author))

        connection.commit()
        connection.close()

    def mark_read(self, name):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))

        connection.commit()
        connection.close()

    def get(self, name):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books WHERE name=?", (name,))
        res = cursor.fetchone()
        book = {"name": res[0], "author": res[1], "read": res[2]}
        connection.close()
        return book

    def delete(self, name):
        connection = sqlite3.connect(self.data)
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=?", (name,))

        connection.commit()
        connection.close()
