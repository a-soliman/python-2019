import sqlite3


class DatabaseConnection:
    def __init__(self, datafile):
        self.data = datafile
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.data)
        return self.connection

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type or exc_value or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
