# oop/library_system.py

class Book:
    """
    Base class representing a general book.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """

    def __init__(self, title: str, author: str):
        """
        Initializes a Book instance.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    Attributes:
        file_size (int): The file size of the eBook in KB.
    """

    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes an EBook instance, calling the base class constructor.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the eBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Attributes:
        page_count (int): The number of pages in the printed book.
    """

    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a PrintBook instance, calling the base class constructor.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the printed book.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Class representing a library that contains books.
    Demonstrates composition by holding a collection of book objects.
    """

    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book (Book, EBook, or PrintBook) to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books currently in the library.
        """
        for book in self.books:
            print(book)
