# Video 1 : The very basics of programming - "Hello, World!"
*[Title screen]*
We've look at some theory, but now it's time for practice! Today, we'll be looking at how we can write our first piece of real, runnable code. We will be starting with no assumed knowledge of Python or coding, but a basic sense and understanding of the logical and *algorithmic* thinking we may want to use when approaching writing our first piece of code - only as much as we covered in the very beginning of this course.

Python is just one programming language of literally *thousands* that are out there, but it's the only one we need concern ourselves with in this course. It's easy to pick up, easy to understand, and is one of the most widely used languages for machine learning and AI.

## "print", and Your first line of code
*[subtitle card]*
The first thing we want to in Python is get to grips with "print" - which is what we use to get our program to write human readable messages when we run it. Print is the very first *function* we're going to use, we'll learn more about functions a little later in the course, for now just understand that they are calls for the program to do *something*, usually taking one or more *augments*. Print is often used so we can see what our program is doing while its still running, or to give a quick message on what it has done once it finished. For now, we're just going to have a bit of a play around with it!

In python we write them like this: `print()`, that's the name of the function we want, followed (no space!) by opening and closing brackets. It's inside those brackets *[gesturing to/highlighting the brackets]* we put our arguments. Remember, print is used to write messages, so our argument is whatever we want that messages to be. It's something of a tradition in programming when learning a new language to have you're first printed messaged be "Hello, World!", so that's exactly what we're going to do.

`print("Hello, World!")`

And that's it, we've got our first line of code! We can run this right now; the computer will get to this line, it will se we're calling a function 'print' with the argument "hello, world", and it already knows what that means, so it does everything it needs to in the background, and writes our message!

Of course, it doesn't need to just be hello world it can be anything I want, I could write my name here, my favorite number, I could write out the entire script of my favorite movie, I could even leave it blank and whatever it is, the computer will write it.

# Variables
*[subtitle card]*
I mentioned I could use print to write out my favorite number - but what if I'm indecisive and I pick a new favorite number tomorrow, and don't want to go to the effort or re-writing my print statement? This is when we would use *variables*.

It's very easy to define variables in Python, we just give it a name and then define what we want it to be using the equals symbol and some value on the right

`my_number = 5`

And we can then use this variable anywhere we want to refer back to whatever we defined it as.

`print(my_number)`

The eagle eyed amongst you may have noticed that we didn't use the speech marks we did in our "hello world" example. We only use them when we're writing *strings*, human readable pieces of text. We're going to learn more about exactly how that works in *data types* section, for now just keep it in the back of your mind and remember: plain text - speech marks, numbers and variables names - no speech marks.

Going back to my_number, we can now change this any time we want and it's value changes with it. This is super helpful if we want to reference the same value at multiple points in our code, but only want to have to define it once, that way if we need to change it, we only need to change it's original definition.

`my_number = 15`
`print(my_number)`
`print(my_number)`

We can even redefine or update variables, that's give them new values after we've already defined them. Just remember that Python code is run sequentially line by line, so whenever we reference a variable it's going to be whatever it was *most recently* defined as at *that point* in the code.

`my_number = 15`
`print(my_number)`
`my_number = 16`
`print(my_number)` is different to...

`my_number = 15`
`my_number = 16`
`print(my_number)`
`print(my_number)`

The only thing we CAN'T do is reference variables that don't exist, or at least haven't been defined yet by that line. This will cause an error or *Exception*, and usually when a program encounters an error it will just give up and stop working, which obviously we want to avoid!

`print(not_defined)`

`print(my_other_number)`
`my_other_number = 0`

## Introducing mathematical expressions
*[subtitle card]*
Briefly, to lead us onto our next topic, we're going to introduce some mathematical operators we can use in Python. Have a look at this:

`my_number = 1+1`
`print(my_number)`

This works pretty much how you'd expect it to. We've defined my_number as 1 plus one, which we know is 2, and now every time we reference my_number we get the value 2. This doesn't just work for variable definitions, we can use it directly in the print statement.

`print(2+2)`

And we can write expressions that reference other variables

`var1 = 5`
`var2 = 7`
`var3 = var1 + var2`
`print(var3)`

pretty much anywhere we can write a number or a variable, we can write a mathematical expression. Obviously, we can do a lot more than just basic addition, but THAT is what we're going to be talking about in our next topic!



# Video 2 : Maths through programming
*[Title card]*
We've introduced the idea that we can use code to manipulate numbers, now we're going to explore that in a bit more depth. Maths is one of the most fundamental elements of computing - arguably, ALL of computing is just maths, as everything a computer does it does by manipulating numbers behind the scenes! *[1s and 02 graphics or something]*
