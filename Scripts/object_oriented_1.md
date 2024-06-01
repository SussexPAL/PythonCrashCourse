# Object oriented programming part 1: introductions
By now, we've seen a good amount of the fundamental things Python is capable of. We've seen how we can use, and define our own, functions. We've explored the base data types we'll be using, and some of the more high-level ones like dictionaries and arrays.

One of the last fundamental features of Python we've yet tackle is that of *classes* and *object oriented programming* *[very simple diagram of a 'class' with multiple 'objects' coming off of it]*. Using classes and object, we can define ways to structure data, and run functions, or use ones that have been defined by other developers. This is an invaluable tool for designing and organizing our programs in a way that is both efficient for the computer at the low level, and intuitive and easy to visualize for us at a high level. While it can be initially difficult to wrap one's head around when first learning to code, it becomes much simple very quickly once you've grasped the fundamentals. Today, we'll be going from having no knowledge of OO programming, to (hopefully) it feeling like second nature.

## What are classes?
A simple way to think of classes is to first think back to functions. We know that using functions, we can define our own processes along with the data we want to go into them, and the data we want to come out (what we want them to return). We can then use these functions again and again, almost like little mini-programs inside our program, in different contexts. Classes are similar: they're things we can define ourselves (or use inbuilt/imported ones) to be re-used in our program with different parameters. Only, while functions tell our program what we want it to DO, classes tell our program what kind of items and objects we want it to HAVE (remember that word 'objects' for later). Think of functions as verbs, thing that is done, and classes as nouns, things that are.

Let's look at an example. Classes are used often as representations of real tangible things. Let's say we want a way to represent students at a university in our program *[some kind of empty box labeled 'Student']*: first we would ask ourselves what about each student we want to represent - for the purposes of this example we'll say we need to know *[appearing as a list in the box graphic]* their name, and which year of study they're in. Already we have a pretty good template for what a student would look like. Note how we haven't said what any of these values actually would be *[cycle through some example values, name="bob", year of study=1 etc but ultimately leave it blank]* only that they are there, and that (crucially) they could be any number of possible values; they're like variables for each student. We call each one of these template-values "fields" or "properties". *[caption/circle/whatever list of properties as 'properties']*

Next, we might think about what we want individual students to be able to DO, or what might happen with them. Lets's say we want a student to be able to introduce themselves with a short message *[speech bubble "hello, my name's __, I'm a year __ student" from student box]*, and to continue into the next year, thus increasing their year of study by 1. *[add list containing introduce_self and continue_year to student box]* This gives us two clearly defined actions we want each individual student to be able to take, we call these *methods* *[label above list as methods]*. If fields were like variables inside class, think of methods as being like functions.

## What are objects?
This template - which tells us what want to know about each student, and what we want them to do - is our *class*. It is using this class that we declare each individual student. these individual students are our *objects*. *[diagram of multiple student objects with their own different value for name and year of study]*.

Once an object has been instanced (created) they become their own thing! Separate from any other objects, and from the class itself (even though it's still based on the class). If we change any of that object's fields, they will be changed for that object only. If we call any methods from that object, it will be called from that object only. This doesn't mean that objects can never interact with each other, we can even define methods in the class explicitly for interaction between objects if we want *[maybe a new example method, `meet_student`, just showing one student calling it's own introduce method, then calling that of another student]*, just that they are separate.

## Defining the constructor
We've learned what classes and objects are in theory. In practice, how can we implement them in Python? Python has it's own syntax for defining classes:
`class Student:`
`   # More here in a sec...!`
Here we've started to define our own class using the *class* keyword. We've given it a name, starting with a capital letter by convention. The block below this line will be where we define our properties and methods. See how this looks very similar to how we define functions, only this time the keyword is different *[highlight `class` keyword]* and we leave out the brackets.

Before we move on, there's one more thing to explain. Most implementations of OO programming (including Python's) utilize something called a constructor. The constructor is a special method which all *[well, most]* classes will have, which is run as the very first thing after a new object is instanced, in order to populate it (fill out it's fields) and do any other set up work that might be needed.

*[show a newly created student with values of ??? for name and year, then being run through a constructor, and having it's fields filled in]*

In Python, the constructor is written like this:
 `class Student:`
`   def __init__(self, name, year):`
`       self.name = name`
`       self.year = year`
Seeing as how we've already covered the basics of functions in Python, you should be able to make some sense of what is going on here, however you may be left with a few questions:
* What does 'init' mean, and why the double underscores on either side?
* what is 'self'?
* Why does it look like we're defining variables as themselves?
Let's address those.

Firstly, 'init' is short for initializer (which is another term for constructor). And, yes, it *does need* to be called that, if we tried giving it any other name, Python wouldn't recognize it as a constructor. This is because 'init' belongs to a special group of methods with pre-decided names, sometimes called 'magic methods' or 'dunder methods', which have their own special syntax reserved for calling them *[maybe a list of some others like __add__ or whatever]*. Of these magic methods, init is the only one we need to understand today.

Next, the *self* field. As you may be able to guess, 'self' refers to the individual object of the class in question. In the case of the 'init' constructor method, this is the newly created object which we want to fill in the fields of. Every method of a class (with a few exceptions we won't be covering today) requires the 'self' object to be the first parameter of the method *[reminder: thats the bit in brackets]*, even if the method doesn't have any other parameters otherwise. Fun fact unlike 'init' and the other magic methods, we don't *need* to call it 'self', we can give it any valid name we want it it will still work, however out of convection 'self' is the name that's used pretty much everywhere, so it's recommended that we stick to it.

Lastly, let's break down the syntax of the body of the method, and why it looks like we're defining a variable as itself. We'll focus on the first line *[focus on the first line]* as both lines work the same way. the key thing to note is that the variable we're assigning to isn't just 'name', it's `self.name` *[underline the `self.`]*! In Python, this syntax refers to the field 'name' of the object 'self', which remember is our brand-new object that we're constructing. `name` and `self.name` are actually two completely different variables *[underline/highlight both in different colours]*! And because 'self' is brand new `self.name` is empty - what this line does is define it as the value of `name`, one of the parameters of the constructor [arrow going from `name` in parameters to `name` in the assignment line, then another arrow going from `name` to `self.name`]. 

After running this constructor, we'll have a shiny new object with two fields filled in!

## The constructor in action
Now we have a simple Python class definition, including a working constructor, how do we go about creating objects of our own, IE *calling* the constructor we just defined? This is actually (you'll be relieved to hear) the easiest part. All we do is write the name of the class followed by brackets.
`Student()`
And inside those brackets we fill in the parameters we defined in the constructor EXCEPT for self. We never need to explicitly fill in 'self' as Python does it automatically any time we call a method!
`Student("Grace", 1)`
Perfect! You'll notice we didn't actually call the constructor by it's name `__init__`, this is because we don't need to. Again, Python does that automatically whenever we call a new object to be created. If you like, you can imagine the constructor as being a function which shares the same name (capital letter included) as the class it's defined for. While this isn't *quite* accurate to what Python really does behind the scenes, it is a helpful way of remembering the syntax as you'll be using it. Only thing we need to do now is actually store our new object, can do this by:
* assigning it to a variable
`student1 = Student("Grace", 1)`
* Adding it to a list
`students_list.append(Student("Grace", 1))`
* In a dictionary...
`students_dict["grace"] = Student("Grace", 1)`
or really anything we can do with any other data in Python!

## Roundup
So, we've introduced OO as a concept - we know what classes are, we know what objects OF a class are, and we've taken our first look at how we can define and use them in Python. In the next few sessions *[episodes? whatever]* we'll be looking at how we can use Python to define methods, some more advanced uses of fields, and later introduce the idea of inheritance, what it means in the *theory* of OO, and how in *practice* it's done in Python. But for now, we should take some time to review what we've just learned and really internalize OO as a new concept before moving on later.
