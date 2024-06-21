# Object Oriented Programming part 3 - Class interaction
This session, we're going to take a look using multiple classes together in a single program, and how methods can allow different objects to interact with each other. We wont't actually be covering any new ground, that is we won't be introducing any new features we haven't seen already, but we'll be using them in new and more complex ways. 

In fact, we'll be seeing our first real emergent complexity from everything we've learned so far working together in a single relatively big, program.

Also it's a good idea to make sure you are aware of the difference between passing by reference and passing by value, and when and why Python does each. We do have a video on this, which you may also go back and review at any point. 

## Defining multiple classes
As you probably assumed, we can absolutely define multiple classes in the same Python program, just like how we can define multiple functions or variables. Let's add some more classes to our student example:

Say in our model university program we don't just want students, we want books and a library as well. Let's consider writing classes for each.

*[cut away to class diagrams here]*
Our books should have:
* a title
* an author
* a year of publication

Our library should have:
* a list of books
* a set of students who are 'members'

*[Extra requirements on a separate list]*
We also want these classes to work together.

We should be able to:
* register students at a library
* have students check out a book from a library, but ONLY if they are registered

## Some new classes
Let's get started.

Simplest to define will be the books. We're going to write a book class with 3 fields, all of which are passed as arguments to the constructor.
~~~ py
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
~~~
See also that we've added some type hints, which we learned about in our 'further functions' session!

Let's now modify our student class so that they can have a book of their own. For the purposes of this exercise, we'll say a student can only have one book at once.
``` py
class Student:
    def __init__(self, name):
        self.name = name
        self.year = 0
        self.book: Book = None
``` 
This is as simple as introducing a new field to the class definition. Note that we haven't given it as a constructor parameter, and by default the property is 'None'. A newly created student will have no book.

We can set objects to be properties of other objects! In fact classes, once they've been properly defined, can be though of just like any other data type, and used in much the same way. See also that we've used type hinting, saying we want this property to be of type 'Book' - we use this syntax to type-hint variables.

Finally, let's write our library class. Starting as usual with the constructor.
```py
class Library:
    def __init__(self):
        # Notice the constructor doesn't take any parameters: all properties are given default values
        self.book_shelf = []
        self.members = set()
```
This time the constructor doesn't take ANY arguments, every field is given some default value. That is:
* an empty list for the book shelf, this is where the books in the library will be stored
* an empty set of members, for the students who have registered to the library

## Adding functionality
First let's allow students to register to a library. We will do this by adding a method to the library class.
```py
    def register(self, student: Student):
        # This method registers an existing student to be a member of the library
        # unlike new_book, this doesn't create a new Student, instead one is passed-by-reference as an argument
        if student in self.members:
            print(student.name + " is already a member.")
            return
        
        self.members.add(student)
        print(student.name + ", welcome to our library!")
```
This method will take a Student object (can you see that type hint in the parameter?) and checks to see if they are already a member using the `in` keyword against the `self.members` set. Not they are added to it, otherwise the method returns early. In either case a brief message is printed out.

We could also have implemented this same functionality by writing a method of the Student class. Let's see what that might have looked like.
``` py
    # In the Student class
    def register(self, library: Library):
        if self in library.members:
            print("I'm already a member of that library!")
            return
        
        library.members.add(self)
        print("I have now joined the library")
```
See how similar it looks - because it is doing the same thing, just from a different place. We don't need both, just one, but if you do want to include both it a good idea to have one just be a call to the other in disguise. This saves you work, and prevents discrepancies.
``` py
    # In the Student class
    def register(self, library: Library):
        # This is much better!
        library.register(self)
```

Next, we want to populate a library with books. We're going to write this one a bit different; rather than taking a book as a parameter, this method will create a new book based on the parameters given.
``` py
    def new_book(self, title: str, author: str, year: int):
        # This method calls the book constructor itself!
        book = Book(title, author, year) 
        self.book_shelf.append(book)
```
The actual variable 'book' is local, and so won't stay stay in memory outside of this method. But the actual OBJECT will persist, as it gets added to 'book_shelf', a property of the library. So long as the library object stays in scope, the book will too.

Now we're going to add a method to allow a student to borrow a book from a library. Again, there are different ways we could do this. We could have this be:
* a method of the student `student.borrow(book, library)`
* a method of the book `book.borrow(student, library)`
* Or a method of the library `library.loan_book(book, student)`
* We could even write it as a global function `borrow(book, student, library)`
Which one we choose depends on what we think is the design for our program. We're going to add it as a method of the library.

Remember that we're storing our books in a list in a library. Instead of passing the book as an object, we'll want to reference them by index number. We'll start like this:
``` py
    def loan_book(self, book_idx, student):
            if student not in self.members:
                print("sorry, you're not a member of the library, why not register?")
                return
```
We only want books to be accessible to students who are a member of the library, so the first thing we do in this method is to check if the student is not a member - if not we print a message and return from the method early.

We also want to check that if the student already has a book on loan, for this we can an implicit 'is not None': any variable, like our book property of the student, will be read as 'False' if it is None - basically checking of the variable is empty!
``` py
        if student.book: # This is like saying "is not None"
            print("Sorry, you already have a book on loan")
            return
```

Lastly, we want to prevent a student taking out a book that another student already has! We can do this another implicit 'is not None' check, only this time we want to know if it IS none, so we use the 'not' keyword.
``` py
        if not self.book_shelf[book_idx]:
            print("Sorry, that book has already been taken out")
            return
```

Now the actual functionality. We want to remove a book at the given index from the bookshelf - replacing it with a None (like an empty space on the shelf). We that want to give that book to the student. Finally, just to be nice, we'll print out a little message!
``` py
        # Take the book of the shelf
        # Fill in the index-space we took it from with None
        book = self.book_shelf[book_idx]
        self.book_shelf[book_idx] = None

        # We then give the book to the student
        student.book = book

        print("Thank you, " + student.name + ", enjoy " + book.title)
```

Here's what it all looks like, feel free to return to this later or pause as long as you need.
``` py
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
```

## Seeing it in action
We're now going to walk through using the classes we've just defined. Let's say we're writing a completely fresh program that has imported the class definitions we just wrote
*[SIDE NOTE: 'importing' is how we reference code from one Python program in another, it vital for big projects!]*
``` py
from oo_example import Student, Book, Library
```
Let's get started.

The first thing we're going to do is define some objects, we'll go for 4 students and one library. We're going to do this by calling the constructor for each Class.
``` py
student1 = Student("Mika")
student2 = Student("Rick")
student3 = Student("Vivian")
student4 = Student("Neil")

campus_library = Library()
```

We're now going to populate our library with some books. 3 books would be disappointingly few for a real library, but it'll be enough for this example
``` py
campus_library.new_book("Waiting for Godot", "Samuel Bucket", 2014)
campus_library.new_book("Waiting for Blender", "Delia Jeanna", 2015)
campus_library.new_book("Waiting for Linux Desktop", "Zoë B'Text", 2016)
```

We should see that the library will not allow books to be borrowed by students before they have registered - but once they have registered they may borrow up to one book at a time.
``` py
# CALLING METHODS
# Trying to borrow without registering
campus_library.loan_book(0, student1)
campus_library.loan_book(1, student2)

# Registering
campus_library.register(student1)
campus_library.register(student2)
campus_library.register(student3)
campus_library.register(student4)

# Borrowing books
campus_library.loan_book(1, student2)
campus_library.loan_book(2, student3)
```
We should also see that no student can borrow another book if they have already taken one out, and no student can borrow a book that has been taken out by someone else.
``` py
# Trying to borrow a second book
campus_library.loan_book(0, student2)
campus_library.loan_book(0, student3)

# Trying to borrow a book someone else already has
campus_library.loan_book(1, student1)
campus_library.loan_book(2, student4)
```

## Summary
This has been a run through of how we can get multiple classes to interact with each other - which we've seen by writing our first real complex, multi-part program!

If this felt like a lot - even if you didn't understand all of it at once - do not worry! We've come a long way from "Hello, World!", and this material isn't going anywhere, you can review it and take it at your own pace as long as you need. 

The complete code for what we wrote in todays session is available, its a good idea to look through it yourself whatever level of understanding you feel you're currently at. Go through it, use it, tweak it, even try re-writing it for yourself!

We're almost at the end of the programming fundamentals section of this corse. We have one last feature of OO programming yet to cover - inheritance - then you'll have everything you need to begin tackling programming and moving onto machine learning for yourself.