# This is pretty much identical to the student class we defined when first introducing OO
# only, we have added one new property (for a checked out book)
# and one new method, for returning 
class Student:
    def __init__(self, name):
        self.name = name
        self.year = 0
        self.book = None
    
    def register(self, library: 'Library'):
        # Just a call to another method, in disguise...!
        library.register(self)


# This class represents a book with a name, an author, and a year of publication
# beyond that it doesn't do much exciting
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


# This is our library class - the most complex class we've done so far!
# But don't be intimidated, everything we do here we HAVE done before (if maybe in more simple contexts)
# and we'll explain everything as we go along, both here in the comments, and in the video/transcript where we introduced it
class Library:
    def __init__(self):
        # Notice the constructor doesn't take any parameters: all properties are given default values
        self.book_shelf = []
        self.members = set()

    def new_book(self, title: str, author: str, year: int, idx=0):
        book = Book(title, author, year)
        self.book_shelf.append(book)

    def register(self, student: Student):
        # This method registers an existing student to be a member of the library
        # unlike new_book, this doesn't create a new Student, instead one is passed-by-reference as an argument
        if student in self.members:
            print(student.name + " is already a member.")
            return
        
        self.members.add(student)
        print(student.name + ", welcome to our library!")

    def loan_book(self, book_idx, student):
        # This method loans a book to a student, keeping a log of it in the loans field
        if student not in self.members:
            print("sorry, you're not a member of the library, why not register?")
            return

        if student.book:
            print("Sorry, you already have a book on loan")
            return
        
        if not self.book_shelf[book_idx]:
            print("Sorry, that book has already been taken out")
            return

        # Take the book of the shelf
        # Fill in the index-space we took it from with None
        book = self.book_shelf[book_idx]
        self.book_shelf[book_idx] = None
    
        # We then give the book to the student
        student.book = book

        print("Thank you, " + student.name + ", enjoy " + book.title)