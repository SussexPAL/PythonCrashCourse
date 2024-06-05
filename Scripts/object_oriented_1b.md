## Rounding out the basics of OO in Python
## Rounding out the basics of OO in Python
By now, we have a good idea of what Object Oriented programming is, even if it still seems like a relatively new concept. We know about classes, how have fields and methods, and how multiple separate objects can come from one class. We've also taken our first look at how OO is done in Python, how a special method called the constructor (or 'init' short for initializer) should work, how we define it, and how we use it to instance new objects of a class.

We're now going to explore in greater detail the different fields and methods a class might have, what they might be used for, and crucially how we implement and handle them in our own Python code.

## Defining our own methods
## Defining our own methods
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

Beyond that, class methods are really just like any other functions. They can take any number of parameters of any type, they can return value, and they can call other functions and methods internally.

## More about properties
Now we've seen how we define and access class fields (or properties) for classes in python. So far it's been pretty simple: we define a field in the class definition, we write our constructor such that it takes an argument for that field, then every time we run that constructor we pass in the values we want. But, don't get the idea that there's a strict 1 to 1 relationship between properties, and constructor parameters, because this is not always the case.

To illustrate this let's introduce an entirely new example. Let's define a class to represent a 2d square, with a single property for it's area.
*[some kind of class diagram for class square with 1 property area]*

You may be imagining a constructor that looks something like this:
`class Square:`
`   def __init__(self, area):`
`       self.area = area`
And you wouldn't be wrong, this is a perfectly good solution, but it's not what I want to show you for this example. You probably know the area of a square can be calculated as the length of one of it's sides squared. We can define a constructor that does exactly this: takes a parameter for length, and from that calculates area.
`class Square:`
`   def __init__(self, length):`
`       area = length ** 2`
`       self.area = area`
This illustrates our earlier point. The constructor for this class takes a parameter, which is not directly stored in a field. Similarly, the area property is not directly given as parameter. Instead, it is calculated based on the parameter given.
*[in action]*
rect = Rectangle(2, 4)
print(rect.area)
*[but this line gives an error, because there IS no length field]*
print(rect.length)

It's also not uncommon for classes to assign static default values to certain fields in the constructor. It's tweak our earlier Student example to always start with a default value of 0 for year_of_study:
 `class Student:`
`   def __init__(self, name):`
`       self.name = name`
`       self.year = 0`
See that the `year` parameter has been removed all together, but the `self.year` property remains, and is assigned the same default value each time. But this doesn't mean the value has to STAY at 0 for the lifetime of each object. To illustrate this, we'll use the `continue_year()` method we defined earlier:
`stu1 = Student("Alan")`
`stu2 = Student("Ada")`
`print(stu1.year)`
`print(stu2.year)`

`stu2.continue_year()`
`print(stu1.year)`
`print(stu2.year)`

## roundup
This pretty much covers the basics of OO in Python, although we've only just scratched the surface of how we can actually apply them. Again, practice is key: having a play around, and doing some simple challenges with what we've show so far is a great way to digest these concepts.

In the next session, we'll show some more complex use of Objects.