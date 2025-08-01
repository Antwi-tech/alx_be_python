# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book object to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find the book by title and check it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book titled '{title}' is not available for checkout.")

    def return_book(self, title):
        """Find the book by title and return it if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book titled '{title}' is not currently checked out.")

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
