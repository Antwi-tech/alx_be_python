# oop/book_class.py

class Book:
    """
    A class to represent a book with title, author, and publication year.
    Demonstrates Python magic methods: __init__, __del__, __str__, and __repr__.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method that initializes the book attributes.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method that is called when an instance is deleted.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a human-readable string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the book that
        could be used to recreate the instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
