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
    print(str(num) + " is even!")
else:
    print(str(num) + " is odd.")
```
But I don't just have one number I need to do this for, I have several. A for loop might help, if they're all in a list:
``` py
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!")
    else:
        print(str(num) + " is odd.")
```
But what if I need to do this in two different places in my code, then I'd need to write the whole thing out twice:
``` py
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!")
    else:
        print(str(num) + " is odd.")

# Some more code here...

numbers = [6, 7, 8, 9, 10]
# But we already wrote this :(
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even!")
    else:
        print(str(num) + " is odd.")
```

[CENTER CAM]
This is where functions come in. In Python, we can write a small (or, for that matter, a very large) section of code and give it some name. We can then refer back to it by this name later on in the code whenever we need it. A bit like how we store data in variables for re-use - only instead of data, it's actual code that we can run!
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
        print(str(x) + " is even!")
    else:
        print(str(x) + " is odd.")
```
And we can find out that it is, in fact, even as many times as we want - but that doesn't help us with any other number!

Okay, so maybe we leave the definition of x outside the function.
``` py
# Defining x outside the function
x = 4

def is_even():
    # Reference x inside the function
    if x % 2 == 0:
        print(str(x) + " is even!")
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
But now is_even can't run without variable x! What if we need x for something else, or forget to change it, or forget to define it all together? Sure, this works, but it's far from ideal - there's too many things that could go wrong! *[SIDE NOTE: and anyway, overusing highest scope, aka GLOBAL variables, like this is considered bad practice!]*

[CENTER CAM]
But, luckily for us, there's a solution. And it's got everything to do with those brackets
`def is_even():` *[highlight brackets]*

## Passing parameters
If we want our function to not just work, but work in lots of different contexts, we can start introducing parameters.
`def is_even(parameter):` *[highlight brackets]*

[SIDE CAM]
A parameter is like a piece of information which needs to go into a function in order for it to know what to do, and we use them pretty much just like variables, only instead of declaring and defining them, we just name them inside the brackets.
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
        print(str(x) + " is even!")
    else:
        print(str(x) + " is odd.")
```
See how x is now a parameter, meaning it will take whatever value gets passed to the function each time it is called. We can now use it again and again whenever we want, passing whatever value we need (IE the number we want to know if it's even or not) as the argument each time.
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
We want to avoid a misconception you might have at this point: parameters are not the same as the variables we define ourselves - similar, but not the same. The important difference is in how they are declared. While variables require an explicit value to be defined as, parameters wait to be given the value that is passed to the functions. 

For this example, x is left blank until the function is called, at which point it takes on the value of whatever argument was passed in brackets:
```py
is_even(5) # So function runs with x = 5
is_even(50) # So function runs with x = 50 
```

## Multiple parameters
It's important to remember that whenever we call a function, it needs to be passed the right number of values, that is one for each parameter we defined. If we forget to do this, we get an error!
```py
is_even() # Well, what is x supposed to be, then!? >:(
``` 
I say "the right number of", because we can define functions with as many parameters as we want, that is; none, one, or many. If we have more than one parameter, just need to make sure they have different names, and are comma separated. Just remember that the order is important.
```py
def add(num1, num2):
    num3 = num1 + num2
    print(str(num1) + " plus " + str(num2) + " is " str(num3))

add(2, 4)
add(6, 8)
```

[CENTER CAM]
## Return values
So far so good, but take a look at this: we're going to use our function as the condition in an if statement.
``` py
# Using our function in an if statement
if is_even(2):
    #do something...
    pass
```
It's obvious what we're trying to do, we have an if statement that we want to trigger if 2 is even. But there's a problem. We know that if statements need boolean expressions, or at the very least something that can be cast to a boolean. `is_even(2)` isn't a boolean, its a function call. If we try and run this code, we'll get an error.

[SIDE CAM]
But this is ridiculous, is_even DOES TELL US whether a number is even or not, that's what the print statements are for! But remember what we said all the way back at "Hello, World!", 'print' is meant for us, the human reading what the code is doing on the command line. Printing doesn't tell the program itself anything, we can't make our program read back what its just printed - unfortunately, that's just not how it works. *[SIDE NOTE: maybe it would be possible, but even thinking about it is giving me a headache]*

What we want is for our function is_even() to somehow give us an actual boolean value we can use. So what can we do? Well, we know we use parameters pass data IN to a function, is there a way we can define what data we want to come OUT of it?. This is where we use return statements. The return statement is actually very easy to use: you just write the return keyword, followed by the value you want to come out of the function.
``` py
def is_even(x):
    if x % 2 == 0:
        print(str(x) + " is even!")
        return True # Exists the function, returning true
    else:
        print(str(x) + " is odd.")
        return False # Exists the function, returning true
```
Once a function hits a return statement it will exit out of the call with whatever value we've given it. This value can be a variable, and expression, even another function call - here we're giving it a literal boolean. Now, depending on what value x is passed to it, is_even will output either True or False. It's ready to be used in an if statement.

[CENTER CAM]
## Recap
Learning about functions is probably the biggest leap forward we've taken since we started all the way back with "hello world" *[some little "Hello, World!" graphic here would be cute!]*, so it's okay if it takes a little while for these new concepts to properly sink in, or if you still have questions. We're going to take just a minute to review.

[CUT AWAY]
Recall all the way back to learning about expressions - we said any expression, no matter how long or convoluted it looked to us, would AT RUNTIME (that is to say, when the program runs) be evaluated down to a single value.
```py
exp1 = (1 + 0.5 + 1.5) * 2 / 3 + (5 ** 2 % 4) # This is literally just 3.0
print(exp1)
# See?
```
Functions - and function calls - work in much the same way, where the value that they are ultimately evaluated to at runtime, is the value that the function returns.
``` py
def literally_just_3():
    return 3.0

exp2 = literally_just_3()
print(exp2)
```
This works no matter how many, or how few, parameters your function takes, what your functions does with them, or even if it ignores them all together.
``` py
def add_then_double(num1, num2):
    return (num1 + num2) * 2

exp3 = add_then_double(2, 3)
print(exp3)
```
And maybe now you're wondering "do we need a return statement? earlier we left it out and the function worked just fine?". Well, no! If a function has no return statement it gets evaluated to None - remember we learned about None when we looked at data types! This is just one of the reasons why having the NoneType is so important.
```py
def no_return():
    oops = "no return statement!"

exp4 = no_return(100)
print(exp4)
```

## Summary
[CENTER CAM]
In computer science, we like to generalize functions as black box. That is, when we call a function, we put values in, and a value comes out again. Once we have that final value in return we can no longer know, nor should we really care, about exactly how the function works inside.

Which isn't to say what a function does isn't important - it's hugely important. The return value needs to be correct - IE it needs to do what we want it to do - and it should do it in as efficient (that is, quick) a way as possible. But these are things we need to consider when writing the program - and before we run and call those functions.

With this, we've covered all the fundamentals we need to know about functions. Now would be a great time to do some exercises, to see how they work for yourselves, and hopefully strengthen your understanding as much as possible

*[END HERE IF WE DON'T END UP DOING THIS NEXT BIT AS IS LOWER PRIORITY]*

Next, we're going to take a look at some of the advanced features and uses of functions, as well as some of the tricks that Python - as a language - has built in to make working with them more flexible.