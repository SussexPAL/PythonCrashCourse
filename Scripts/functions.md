# Functions
One of the core principles of good programming is: avoid repetition -- "say something once, why say it again?". This is a big part of why loops, which we've just looked at, are so important. This is good practice because
1) it saves space, which is good for US (we need to write it, after all...), and the computer that needs to store it
2) it makes it easier to change later - we only need to change it in one place.

## In Python
[SIDE CAM/CUT AWAY]
Say I've worked out a way to tell if a number is even or odd, and I write it in Python.
``` py
num = 4
if num % 2 == 0:
    print(str(num) + " is even!)
else:
    print(str(num) + " is odd.")
```
But I don't just have one number I need to do this for, I have several. A for loop might help, if they're all in a list:
``` py
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!)
    else:
        print(str(num) + " is odd.")
```
But what if I need to do this in two different places in my code, then I'd need to write the whole thing out twice:
``` py
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!)
    else:
        print(str(num) + " is odd.")

# Some more code here...

numbers = [6, 7, 8, 9, 10]
# But we already wrote this :(
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!)
    else:
        print(str(num) + " is odd.")
```

[CENTER CAM]
This is where functions come in. In Python, we can write a small (or, for that matter, a very large) section of code and give it some name. We can then refer back to it by this name later on in the code whenever we need it. A bit like how we store data in variables for re-use.
``` python
def say_hello():
    print("hello world!")
```
This is done with the `def` keyword, followed by the name we want to give our function, followed brackets - and those brackets have a very important role to play, which we'll get to in a minute. Function definitions (that's what the 'def' is short for, by the way) also follow the same rule of code blocks and scoping as our flow control statements (like if, else, for etc.): see the colon, and how the next line is indented.

[SIDE CAM]
How does this help us with our even-number example from earlier? Sure we can write a function to tell us if 4 is an even number
``` python
def is_even():
    x = 4
    if x % 2 == 0:
        print(str(x) + " is even!)
    else:
        print(str(x) + " is odd.")
```
And we can find out that it is, in fact, even as many times as we want - but that doesn't help us with any other number!

Okay, so maybe we leave the definition of x outside the function.
``` py
# Defining x outside the function
x = 4

def is_even():
    # Reference f inside the function
    if x % 2 == 0:
        print(str(x) + " is even!)
    else:
        print(str(x) + " is odd.")
```
Then if we need to we can just change x
``` py
# Seeing if 5 different numbers are even
for i in range(5):
    # We define x as a new number before running is_even()
    x = i
    is_even()
```
But now is_even can't run without variable x! What if we need x for something else, or forget to change it, or forget to define it all together? Sure, this works, but it's far from ideal - there's too many things that could go wrong!

[CENTER CAM]
But, luckily for us, there's a solution. And it's got everything to do with those brackets
`def is_even():` *[highlight brackets]*

## Passing parameters
If we want our function to not just work, but work in lots of different contexts, we can start introducing parameters.
`def is_even(parameter):` *[highlight brackets]*

[SIDE CAM]
A parameter is like a piece of information which needs to go into a function in order for it to know what to do, and we use them pretty much just like variables, only instead of declaring them the first time we just name them inside the brackets.
``` py
def say_hello(name):
    print("Hello, " + name + "!")
```
That parameter can then be referenced by name inside the function code block.

[CENTER CAM]
In order to run the function with a certain value, we write that value in the brackets when we call the function! this is called passing the parameter, or argument.

``` py
say_hello("world")
say_hello("you")
```
Again remember the rule of scoping. The function definition is its own block of code, meaning that any variable names are local to it. If we try referencing a parameter, or any other variable we define in our function for that matter, after we've left that block of code, we'll get an error.
``` py
def say_hello(name):
    print("Hello, " + name + "!")

print(name)
```

[SIDE CAM]
We can now apply this to our is_even example:
``` py
# is_even definition
def is_even(x):
    if x % 2 == 0:
        print(str(x) + " is even!)
    else:
        print(str(x) + " is odd.")
```
See how x is now a parameter, meaning it will take whatever value gets passed to the function each time it is called. and use it again and again whenever we want, passing whatever value we need as the argument each time.
``` py
is_even(1)

num = 3
is_even(2)

for i in range(3, 6):
    is_even(i)
```

*[WRITER'S NOTE: Not sure if this bit is overkill, just wanted to go over these points incase some people are confused, baring in mind that for some students this is their first exposure to programming]*
[CENTER CAME/CUT AWAY]
*[take another look at is_even definition above]*
Let's briefly recap that, and clear up any question you might have. You might we wondering why we're referencing this variable x *[highlight all occurrences of x in function definition, including is the def line]* which we never actually define, IE there is no `x = 3` or `x = 2 + 2` or anything, so how can we be referencing it here?     

HUGO YOU DIDN'T TALK ABOUT MULTIPLE PARAMETERS REEEEEEEEE!!!

[CENTER CAM]
## Return values
So far so good, but take a look at this:
``` py
if is_even(2):
    #do something...
    pass
```
It's obvious what we're trying to do, we have an if statement that we want to trigger if 2 is even. But there's a problem. We know that if statements need boolean expressions, or at the very least something that can be cast to a boolean. is-even isn't a boolean, its a function call. If we try and run this code, we'll get an error.

But this is ridiculous, is_even DOES TELL US whether a number is even or not, that's what the print statements are for! But remember what we said all the way back at "Hello, World!", 'print' is meant for us, the human reading what the code is doing on the command line. Printing doesn't tell the program itself anything.

So what can we do? Well, we know we can define parameters to define the data we want to go IN to a function, we can define what data we want to come OUT using `return`.