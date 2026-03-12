# main.py
from services import Library
from users.Auth import login, register

def menu(role):
    print("\nLibrary System")
    if role == "admin":
        print("1. Add Book")
        print("2. Remove Book")
    print("3. Show Books")
    print("4. Search Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Sort Books")
    print("8. Exit")

def main():
    print("Welcome to Library System!")

    # Require login or registration first
    role = None
    while role is None:
        choice = input("1. Login\n2. Register\n3. Exit\nChoose: ")
        if choice == "1":
            role = login()  # login() must return "admin" or "user"
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice!")

    # After login
    library = Library()

    while True:
        menu(role)

        try:
            choice = int(input("Enter choice: "))

            if choice == 1 and role == "admin":
                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))
                library.add_book(title, author, year)

            elif choice == 2 and role == "admin":
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
                print("Invalid choice or access denied.")  # for non-admin trying add/remove

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()