[MAIN CAM]
# Flow of control 1: If, then, else
So; we've started exploring some basic programming. right now we're kind of using Python like a simple calculator. There's nothing wrong with this, but, we could go further and have a program where the output vary a lot more. Everything we've written so far does the same thing every time we run it, that is we write lines of code, and when we run the program, those lines are executed on at a time, in the order they were written. 
``` py
thing1 = "Hello"
thing2 = "World!"
print(thing1 + ", " + thing2)
```
but what if we want our program to be more flexible? This is where we start looking at flow of control, ie the ways in which we can manage which lines of code are executed, and when.

Think back to data types and expressions, remember that we covered something called a "boolean" - a value that can be either True, or False, 1 or 0, yes or no. One of the primary uses of these booleans is control flow statements. Say we have a block of code and some boolean expression, and we want that block of code to run if, and ONLY if, that statement evaluates to True. Here's an example
[SIDE CAM OR CUT AWAY]
``` py
password = "321"

# Say we only want the rest of this program to run...
# if password is "123"
print("welcome!")

# Otherwise...
print("incorrect password!")
```
Ignoring that "123" *[zoom in to face for emphasis]* terrible password that you should never use in real life - let's clarify: what we want to happen here, why its impossible knowing only what we've seen so far, and what we CAN actually do to make it work.

We have some variable, which we have called 'password' *[underline/highlight password]*. Here, we've given it a definite value, but let's say we don't know what that value is for now *[black out/cross out "321"]*. We want the rest of our code to behave differently, depending on whether or not 'password' has the value "123", IE if the boolean expression `password == "123"` evaluates to true. If it does, then we want to print out "welcome", otherwise "incorrect password". But we can't do this because so far our code runs line by line, meaning BOTH print statements would run. But there is a solution, and it comes in the form of the if statement.

You can think of "if" as asking the computer "When executing this code, only run it **if** this *condition* is true". The condition being some statement that will result in either True, or False.

We have a few "operators" for checking conditions. The first and simplest is two equals signs - this allows us to check if two values are the same.

For example, `2 == 2`, but, also, `2 == 3 - 1`. This seems fine, but, we can also use variables in place here. Let's say we have a variable named "foo", and, we put the word "hello" into it. In our program, we can write `if foo == "hello"`, and, some code will execute. If we change the value of "foo", the program will do something else instead.

There are other equality statements too. We can use the angle brackets as greater than and less than - it's always nice to remember the sign as being a mouth that's trying to eat the bigger one. For example `4 > 2` and `10 * 3 < 29 + 5`

We can also use exclamation equals as shorthand for "Not equals". For example, `"hello" != "world"`, `3 != 1`, and, `foo != "other_word"` (assuming `foo` is still `"hello"`).

All these operators will resolve down to either True or False - for example, if you write `print("hello" == "hi!")`, you will just see `False`! We can then use other keywords to chain multiple conditions together - for example, `not` will invert the output (e.g. `not "hello" == "hi!"` is `True`).

`or` will be true if one or more conditions are true - e.g. `"4 > 2 or 5 > 10`. Five isn't greater than 10, but, because 4 is greater than 2, the entire statement is true.

Finally, `and` requires *all* conditions in a statement to be true. Taking the same example, `4 > 2 and 5 > 10` - we will get `False` because five still isn't greater than 10. This is regardless of the fact 4 is bigger than 2 - because not *all* of the conditions are satisfied, the entire thing will return `False`.

- For loops

- Refresher on Range keyword (brought up in George's worksheet, but, let's properly explain it)

- While loops