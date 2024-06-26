# Further functions
By now we should have already seen how the basics on functions work - we know that functions can take arguments (or parameters), and give us some return value back. We also know how to define our own functions - what parameters we want them to take, and how we get them to return values.

These are actually all the fundamentals that we need to know, but that doesn't mean there's no more to talk about. In this session we'll be looking at some of the more advanced use cases of functions, as well as some of the handy tricks that python has built in to make working with functions easier.

[SIDE CAM]
## Key word arguments
Remember from last time that we define function parameters in the brackets of our function signature. *[SIDE NOTE: The first line of a function definition, ie `def foo(x, y, z) is called the signature]* We said we had to give them valid and unique names.
```py
accounts = dict()

def register(username, fname, lname):
    if username in accounts:
        print("That username is already taken!")
        return False
    
    new_account = [fname, lname]
    accounts[username] = new_account
    print("registered okay!")
    return True

```
Here is an example of a simple function which takes three arguments. This function takes a username, a first name, and a last name. It then checks to see if that username has already been taken. If it hasn't, the new user's details are stored as a list in the dictionary 'accounts' with the username as the key, and the function returns true - as in 'yes, executed successfully'. If the username HAS been taken the function exits early and returns false - as in, 'no something went wrong'.

*[SIDE NOTE: Having true/false return values as success or failure codes from functions is very useful and quite common!]*

[CENTER CAM]
So far so good - but it's not very flexible; it can ONLY take two argument, can't take less, can't take more - always two. Maybe that's not so much of a problem now, but what if we wanted to extend this to take extra optional details like phone number or email address, or what if we wanted the option to override existing usernames some but not all of the time.

Well we could just define multiple functions. This would work sure, and in some cases it's enough, but all of those functions would have to have different names - you'd need to implement them all separately and then remember which one was which when you needed them. You might end up with...
* register(username, fname, lname)
* register_and_override(username, fname, lname)
* register_with_phone(username, fname, lname, phone_no)
* register_with_email(username, fname, lname, email)
* register_with_phone_and_email(username, fname, lname, phone_no, email)
* register_and_override_with_phone_and_email(username, fname, lname, phone_no, email)
You can see it gets pretty overwhelming pretty fast...

In Python, there is a way to make functions more flexible - so that one function can be programmed to two different things depending on what - and how many - arguments it is given. And it comes in the form of key word arguments.

Key word arguments - sometimes called "kwargs", opposed to "args": arguments - are arguments that may or may not be included in a function call, and if they are not they default back to a given value; typically some empty or failsafe value. We write them as so:
```py
def foo(a_kwarg=0):
    # etc...
```
They are written the same as regular arguments, but with an equals and a default value. We can have as many key-word arguments as we want, we can even include both regular arguments and key-word arguments - although if we do this all your non keyword arguments must come first.
```py
def bar(an_arg, a_kwarg=0, another_kwarg=1):
    # etc...
```

[SIDE CAM]
Let's apply this to our register example, starting with phone number and email.
``` py
def register(username, fname, lname, phone="n/a", email="n/a"):
    if username in accounts:
        print("That username is already taken!")
        return False
    
    new_account = [fname, lname, phone, email]
    accounts[username] = new_account
    print("registered okay!")
    return True
```
Here, we've given both new parameters default values of "n/a", as in not applicable. You'll now see that we can call this function with or without these last two arguments.
``` py
register("mrBlueBox", "David", "Tenant")
register("I<3onions", "Jean", "Pierre", "4321 5678", "chef@kitchen.com")

for item in accounts.items():
    print(item[0], item[1])

''' OUTPUT
registered okay!
registered okay!
mrBlueBox ['David', 'Tenant', 'n/a', 'n/a']
I<3onions ['Jean', 'Pierre', '4321 5678', 'chef@kitchen.com']
'''
```
But what if we wanted to include email and NOT phone number, surely that's impossible because the email parameter hast to come after the phone number. Well actually no, this is whats so good about kwargs - you can write them out of order in the function call, so long as you explicitly state which one is which by name.
``` py
register("Buggy", "Ada", "Lovelace", email="love.ada@thepast.com")
```
This is why they're called key-word arguments!

A common use for kwargs is to add extra options to functions, sometimes in the form of booleans. Let's give the option to override existing usernames:
``` py
def register(username, fname, lname, phone="n/a", email="n/a", override=False):
    if (username in accounts) and not override:
        print("That username is already taken!")
        return False
    
    new_account = [fname, lname, phone, email]
    accounts[username] = new_account
    print("registered okay!")
    return True

register("mrBlueBox", "Mathew", "Smith")
register("mrBlueBox", "Mathew", "Smith", override=True)

'''
That username is already taken!
registered okay!
mrBlueBox ['Mathew', 'Smith', 'n/a', 'n/a']
'''
```

[CENTER CAM]
## Internal functions
We know we can call other functions from inside a functions. You can also define functions within functions - they're called 'internal' or 'nested' functions. This can be super useful if the body of your outer function has to do something relatively complex multiple times - the same reason as why you'd use functions anywhere else, really.

Keep in mind though that an inner function won't be usable anywhere outside its outer function. However, nested functions can be vey useful, and good for organization, just so long as your *absolutely sure* you won't need them anywhere else.

## Introducing recursion
Maybe by now you've thought to ask "hang on, if we can call one function from inside another, can we call a function from inside itself!?". Yes. Yes, you can.

This is called recursion, and it opens up a whole world of exciting possibilities (as well as things that could potentially go wrong) which can be super useful. It's something that really deserves it's own session - but we're going to briefly go over it now. 

Take a look at this example:
``` py
def foo(i):
    print(i)
    i = i + 1
    foo(i)
```
Maybe you think this is just like like an infinite while loop, and will keep running quite happily forever. Unfortunately it's not so simple. Say we call our function foo for the first time, it increases i, and then it calls foo again. Remember that that first function call hasn't stopped yet - and it WON'T stop, not until the new foo call which IT made has stopped. And, of course, THAT one wont stop until its called ANOTHER foo, which will then call another, and another and so on all piled on top of each other.

Unlike while loop iterations, function calls need to be kept active in memory until they terminate. For this example, none of these function calls ever stop - ever return - because they're all waiting for the one above them to stop. Eventually, we ARE GOING to run out of space! 

What happens then, usually, is that the program environment sees what's happening, calls it a stack overflow (a special kind of error), and brings the whole thing to a stop. Sometimes this doesn't happen in time and the OS has to step in, freezing or terminating the program.

If you're very very VERY unlucky, your entire computer might start to slow down, or even crash all together. Don't panic *[PAL'S GUIDE TO THE GALAXY: DON'T PANIC]*, modern systems are VERY unlikely to just let this happen. But still, much better to be careful.

[SIDE CAM]
This has all been doom and gloom, does this mean recursion is just stupid and dangerous? Actually, no - we just need to make sure that the call stack doesn't just keep growing forever. We do this by introducing a "base case", a case in which a recursive call is NOT made, and the process can return. Take a look:
``` py
def foo(i):
    print(i)
    i = i + 1

    if i >= 5:
        # This is our base case
        print("DONE!")
        return i
    base = foo(i)
    return base

print(foo(1))
```
All we've done here is introduce an if statement that will return out of the function once i reaches 10. Let's walk through it in action:

The first time we call foo we pass it a value of i=1. It increases this to 2, and checks to see if it's greater than or equal to 10. It's not - so it calls foo again with i=2. This new call then does the same, increasing i to 3, and making a new call - and so on, and so on, until finally a call to foo is made with i = 9.

This last call increases i to 10 - which means the right condition is met, and it gets to terminate without making another call: it returns 10. You can see that this value then gets returned all the way down the call stack until the call at the bottom finally terminates. We're done, and we get our final value - 10.

This is classic example of a base-and-recursive case function, where the call stack only grows as high as it needs to - that is it keeps growing until some condition (the base case) it met, and the whole stack sort of collapses back to the original call, passing down any return value from the top call with it.

## Type hints
Finally, a brief word on how different data types are used in functions by Python. Say we write a Python function which is meant to take a number, divide it by two, and return it. We'll define it as follows:
``` py
def bazz(x):
    x_div = x / 2
    return x_div
```
How can we know that when bazz gets called x will be a number we can divide, and not some other data type we can't use like a string or a dictionary? 

This is tricky because Python follows a philosophy called 'dynamic typing' where the types of objects like variables and parameters don't need to be explicitly labeled in the code itself - Python is perfectly happy to wait until the program is actually running and just trust everything is the data type it's supposed to be.

But if something ISN'T the right data type, say we call bazz with a boolean, then this is obviously a problem - we can't divide a boolean. Luckily there is something we can do to prevent this. We can introduce type hints for our parameters.
``` py
def bazz(x: int):
    x_div = x / 2
    return x_div
```
See how after variable x we added a colon, plus the name of the type we were expecting.

So what does this actually do? The short answer is: nothing. They're really only there for you, and anyone else you're sharing the code with.

The longer answer is technically nothing, that is Python runtime environment (the thing that actually makes your program run at the very core) completely ignores them. But depending on what extra tools you're using (such as your editor) these type hints can be picked up on, and used to automatically check for potential mistakes or inconsistencies in the code.
``` py
# Uh oh.
bazz("twenty")
```
If one such mistake is flagged up, your editor may alert you to it, a bit like a spelling mistake in a word processor. Some extra tools may even stop the program running before any inconsistencies are resolved.

You can also use type hints for variables...
``` py
number: int = 20
```
and the return type of functions, although the syntax is slightly different: we use this funny arrow, written with a dash and a triangle bracket.
``` py
def bazz(x: int) -> float:
    x_div = x / 2
    return x_div
```

Remember type hints are completely optional! They actually change nothing at the low level. But they are favoured by a lot of people - it can just make your code feel neater if you know what every type is meant to be - especially for people used to other programming languages like Java where this kind of explicit (or *static* typing) is mandatory.

## Summary
With this we've covered everything we need to about functions. Throughout your coding career, you'll be seeing these a lot. You'll be writing your own functions of course, but you'll also have to use ones that have been written by other people. Having a solid understanding of Python functions - both how they work inside, and how they are used - is essential.