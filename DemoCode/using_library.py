from library_simplified import *

# Students
student1 = Student("Mika")
student2 = Student("Rick")
student3 = Student("Vivian")
student4 = Student("Neil")

# Library
campus_library = Library()

# Books
campus_library.new_book("Waiting for Godot", "Samuel Bucket", 2014)
campus_library.new_book("Waiting for Blender", "Delia Jeanna", 2015)
campus_library.new_book("Waiting for Linux Desktop", "Zoë Bo'Text", 2016)

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

# Trying to borrow a second book
campus_library.loan_book(0, student2)
campus_library.loan_book(0, student3)

# Trying to borrow a book someone else already has
campus_library.loan_book(1, student1)
campus_library.loan_book(2, student4)