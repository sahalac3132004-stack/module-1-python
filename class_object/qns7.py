class Library:

    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, title, author):
        book = {
            "title": title,
            "author": author
        }
        self.books.append(book)
        print("Book added successfully.")

    # Display all books
    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nBooks in Library:")
        for book in self.books:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("------------------")

    # Search book by title
    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("\nBook Found!")
                print("Title:", book["title"])
                print("Author:", book["author"])
                return

        print("Book not found.")


# Create Library object
library = Library()

# Add books
library.add_book("Python Programming", "sahal")
library.add_book("Data Science", "john")
library.add_book("Artificial Intelligence", "arjun")

# Display all books
library.display_books()

# Search for a book
library.search_book("data science")