#Question 2 Task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_books(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    book = (title, author)
    if book in library:
        print("Book already exists in library!")
    else:
        library.append(book)
        print("Book added successfully!")
    
def display_books(library):
    if not library:
        print("No Books to Display!")
    else:
        print(library)

def main():
    
    while True:
        print("\nWelcome to the library!\n1. Add Books\n2. Display Books\n3.Exit Library")
        choice = input("Please choose a number: ")
    
        if choice == '1':
            add_books(library)
        elif choice == '2':
            display_books(library)
        elif choice == '3':
            print("Thank you for visiting the library!")
            break
        else:
            print("Invalid choice. Please select again")

main()