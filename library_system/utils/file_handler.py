from models.book import Book

FILE_PATH = "data/books.txt"


def save_books(books):
    with open(FILE_PATH, "w") as f:
        for book in books:
            f.write(f"{book.title},{book.author},{book.year},{book.available}\n")


def load_books():
    books = []

    try:
        with open(FILE_PATH, "r") as f:
            for line in f:
                title, author, year, available = line.strip().split(",")

                book = Book(
                    title,
                    author,
                    int(year),
                    available == "True"
                )

                books.append(book)

    except FileNotFoundError:
        print("Books file not found. Creating new one.")

    return books