"""
LIBRARY MANAGEMENT SYSTEM 

Contains only the requested operations:
1. User sign-up
2. User login
3. Add a book
4. Remove a book

Data is stored in memory and resets when the program closes.
"""

users = {}
books = []
next_book_id = 1


def signup():
    """Register a new library user."""
    print("\nUSER SIGN-UP ")
    username = input("Create username: ")

    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists. Choose another username.")
        return

    password = input("Create password: ")
    if not password:
        print("Password cannot be empty.")
        return

    users[username] = password
    print("Sign-up successful!")


def login():
    """Log in a registered library user."""
    print("\nUSER LOGIN ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}! Login successful.")
        return username

    print("Invalid username or password.")
    return None


def add_book():
    """Add a new book to the library collection."""
    global next_book_id

    print("\n ADD A BOOK ")
    title = input("Enter book title: ")
    author = input("Enter author's name: ")

    if not title or not author:
        print("Book title and author's name are required.")
        return

    book = {
        "id": next_book_id,
        "title": title,
        "author": author,
        "borrowed": False
    }

    books.append(book)
    print(f"'{title}' has been added successfully.")
    print(f"Book ID: {next_book_id}")
    print(f"Borrowed status: {book['borrowed']}")
    next_book_id += 1


def remove_book():
    """Remove a book from the library using its ID."""
    print("\n REMOVE A BOOK ")

    if not books:
        print("There are no books in the library.")
        return

    print("\nBooks in the library:")
    for book in books:
        status = "Borrowed" if book["borrowed"] else "Available"
        print(
            f"ID: {book['id']} | Title: {book['title']} | "
            f"Author: {book['author']} | Status: {status}"
        )

    try:
        book_id = int(input("\nEnter the ID of the book to remove: "))
    except ValueError:
        print("Please enter a valid numeric book ID.")
        return

    for book in books:
        if book["id"] == book_id:
            if book["borrowed"]:
                print("This book is borrowed and cannot be removed.")
                return

            books.remove(book)
            print(f"'{book['title']}' has been removed successfully.")
            return

    print("Book not found. Check the book ID and try again.")


def main():
    """Menu for the four requested operations."""
    while True:
        print("\n LIBRARY MANAGEMENT SYSTEM ")
        print("1. Sign up")
        print("2. Login")
        print("3. Add a book")
        print("4. Remove a book")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            add_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Select a number from 1 to 5.")


if __name__ == "__main__":
    main()
