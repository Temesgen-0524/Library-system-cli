class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed successfully.")
        else:
            print("Book already borrowed.")

    def return_book(self):
        self.available = True
        print(f"{self.title} returned successfully.")

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} | {self.author} | {self.year} | {status}"