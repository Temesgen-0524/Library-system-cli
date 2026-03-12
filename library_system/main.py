from services.library import Library


def menu():
    print("\nLibrary System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Show Books")
    print("4. Search Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Sort Books")
    print("8. Exit")


def main():
    library = Library()

    while True:
        menu()

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))
                library.add_book(title, author, year)

            elif choice == 2:
                title = input("Book title to remove: ")
                library.remove_book(title)

            elif choice == 3:
                library.show_books()

            elif choice == 4:
                keyword = input("Search keyword: ")
                library.search_book(keyword)

            elif choice == 5:
                title = input("Borrow book title: ")
                library.borrow_book(title)

            elif choice == 6:
                title = input("Return book title: ")
                library.return_book(title)

            elif choice == 7:
                library.sort_books()

            elif choice == 8:
                print("Goodbye!")
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()