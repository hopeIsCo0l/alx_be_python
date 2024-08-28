# book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        # Removed the creation message from __init__

    def __del__(self):
        # This will print the deletion message as specified
        print(f"Deleting {self.title}")

    def __str__(self):
        # This returns the string representation of the book
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # This returns the official representation of the book
        return f"Book('{self.title}', '{self.author}', {self.year})"
