# Library Management System

A small command-line library management program written in Python. It provides basic user sign-up and login, plus the ability to add books to a collection and remove books by ID.

## Features

- Register a username and password during the current session
- Log in with a registered account
- Add a book with a title and author
- List existing books and remove an available book by its ID
- Prevent removal of a book marked as borrowed

## Requirements

- Python 3
- No third-party packages are required

## Run the program

Save `library.py` in your project folder, then run:

```bash
python library.py
```

On some systems, use `python3` instead:

```bash
python3 library.py
```

Follow the numbered menu prompts. Choose **5. Exit** to close the program.

## How it works

The program keeps users and books in Python data structures while it is running. Each added book receives an incrementing ID. The remove-book option displays the current collection, asks for a book ID, and removes the matching book if it is available.

## Current limitations

- User accounts and books are stored only in memory, so they are cleared when the program exits.
- Passwords are stored as plain text in memory; this example is not suitable for real user accounts.
- Sign-up and login are available from the main menu, but the program does not require login before adding or removing books.
- Books are initially marked as available. The current menu does not include an operation to borrow or return a book.

## Project structure

```text
.
├── README.md
└── library.py
```

## License

No license is specified. Add a license file if you want to state how others may use, modify, or distribute this project.
