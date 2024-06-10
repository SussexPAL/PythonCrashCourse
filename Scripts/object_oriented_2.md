# Further OO programming
This session, we're going to take a look using multiple classes together in a single program, and how methods can allow different objects to interact with each other. We shouldn't actually be covering any new ground, that is you probably and syntax here that we haven't already introduced, but we'll be using them in new ways just to demonstrate how it all works together, and to see the kind of things that are possible in Python code.

Also, if you haven't already, it would be a good idea to make sure you understand (or at least be aware of) the difference between passing by reference and passing by value, and when and why Python does each. This should make it easier for you to follow what we'll be doing from now on, and to have a basic understanding of how Python handles it behind the curtain. We do have a video on this, which you may also go back and review at any point. 

## Defining multiple classes
As you probably assumed, we can absolutely define multiple classes in the same Python program, just like how we can define multiple functions or variables. Let's add some more classes to our student example:

Say in our model model university program we don't just want students, we want books and a library as well. Let's consider writing classes for each.

*[cut away to class diagrams here]*
Our books should have:
* a title
* an author
* a year of publication

Our library should have:
* a list of books
* a set of students who are 'members'

*[Extra requirements on a separate list]*
We should be able to:
* register students at a library
* have students check out a book from a library, but ONLY if they are registered
* have students return books to a library

Let's get started.

Simplest to define will be the books. We're going to write a book class with 3 fields, all of which are passed as arguments to the constructor.
~~~ py
class Book():
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
~~~
See also that we've added type hints! Remember from our lesson on functions that these are not required, but they can improve the clarity of our code, and provide an additional layer of security - preventing someone passing a string or other object to `year` when we are expecting an integer.