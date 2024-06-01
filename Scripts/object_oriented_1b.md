# Rounding out the basics of OO in Python
By now, we have a good idea of what Object Oriented programming is, even if it still seems like a relatively new concept. We know about classes, how have fields and methods, and how multiple separate objects can come from one class. We've also taken our first look at how OO is done in Python, how a special method called the constructor (or 'init' short for initializer) should work, how we define it, and how we use it to instance new objects of a class.

We're now going to explore in greater detail the different fields and methods a class might have, what they might be used for, and crucially how we implement and handle them in our own Python code.

# Defining our own methods
The first thing we'll look at is how we define and call methods for a class, beyond just the constructor. Once we understand the constructor, moving onto other methods should not be too complicated as the syntax is mostly the same. Let's see this done with our Student class from last time:
 `class Student:`
`   def __init__(self, name, year):`
`       self.name = name`
`       self.year = year`
`   `
`   def say_hello(self):`
`       print("Hello!")`
The `def` keyword is still used, and we still need to include the `self` as the first parameter. Now, however, we can give the method whatever name we want, so long as it doesn't clash with any others in the class. Calling it is also very simple.
`student1 = Student("Grace", 1)`
`student1.say_hello()`
This is mostly the same as calling any other function, only this time we need to specify which object we're calling it for *[underline `student1.`]*. If it looks like we're missing a parameter, remember we don't need to explicitly pass the self parameter for method calls in Python, as this is done automatically.

*[demo method being run]*

Let's add a bit more. We don't just want our student to say hello, we also want them to introduce themselves with *their* name and year of study. Here's how we'd do that:
`   def say_hello(self):`
`       print("Hello! My name's" + self.name + " , I'm in year " + self.year)`
it's as simple as calling back to fields by name which we defined in the defined in the constructor, remembering to use the `self.` syntax. If you're worrying that these fields may not have been defined yet, remember that *by definition* the constructor is the very first that is called when a new object is created. If we're calling any other method from an object, that means the constructor MUST have ran otherwise we wouldn't HAVE an object in the first place! So long as the field has been defined in the constructor, we can reference it later at any time.

*[demo method being run]*

Methods don't just refer back to an object's properties, they can also change them! Let's define a "continue year" method which will increase the student's year of study by one.
`   def continue_year(self):`
`       self.year = self.year + 1`
When run, this will overwrite the self's year property to be it's original value plus one.

*[demo the following being run]*
`student1.say_hello()`
`student1.continue_year()`
`student1.say_hello()`