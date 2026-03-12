from turtle import title

from utils import save_books, load_books
from models import Book


class Library:

    def __init__(self):
        self.books = load_books()

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        save_books(self.books)
        print(f"{title} added to library successfully.")

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]
        save_books(self.books)
        print(f"{title} removed from library successfully.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        for book in self.books:
            print("Available books in library:")
            print(book)

    def search_book(self, keyword):
        results = [b for b in self.books if keyword.lower() in b.title.lower()]
        if results:
            print(f"Search results for '{keyword}':")
            for r in results:
                print(r)
        else:
            print(f"No books found with the keyword '{keyword}'.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
        save_books(self.books)

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
        save_books(self.books)

    def sort_books(self):
        sorted_books = sorted(self.books, key=lambda x: x.title)
        for book in sorted_books:
            print(book)
            