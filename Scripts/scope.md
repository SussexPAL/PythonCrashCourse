# A quick word on scope
This topic will be a brief one, as there's not too much to cover, but it's both:
* an important enough topic that it is essential to understand
* a general enough topic that it wouldn't make sense to squeeze it in anywhere else - it deserves it's own video.
We are of course talking about scope.

We've hinted at scope before, and you may seen some of its effects in your own code - maybe something didn't work the way you expected, or you got an error you didn't understand. Today we're going to break it down.
``` py
def What_is_scope():
    scope = "Let's find out!"

What_is_scope()
print(scope)

'''
Traceback (most recent call last):
  File "c:\Users\PAL\learn_python\scope.py", line 5, in <module>
    print(scope)
          ^^^^^
NameError: name 'scope' is not defined
'''
```

## Recapping blocks
We've already looked at flow of control statements like ifs and loops, and we've looked at how we define functions. This means we should be familiar with the idea of blocks.

To recap, blocks are the ways we separate out lines of code into groups. We need them for flow-control statements to work, otherwise we wouldn't know which lines were part of a statement's body and which were just at the base level.

We know that, in Python, we open a new block with a colon and indentation (that is, whitespace to the left of each line) and stay in that block until the indentation stops.

We know that which block we're currently in depends on the amount of indentation...
``` py
# block a
print("Look at this code!")

def foo():
    # block b
    var1 = 1
    var2 = 20

    if var1 < var2:
        # block c
        var 3 = 300
    
    print("It doesn't actually do anything...")

print("Nothing interesting, anyway.")
```
And we know that blocks can be nested inside of each other: if block b is inside block a, all the code inside block b is still technically is included in block a.
*[class ic blue-j style highlighting of the colours of different blocks overladed onto above]*

In programming, 'scope' has got everything to do with what code is in which block.

## What is scope?
In short, scope is about when and for how long Python stores things in memory. In Python, the scope of any definition (that is functions, variables and *classes* - which we'll get to later) is determined by which block it first appears in. This is easiest to see at the base level:
``` py
# A global scope variable!
my_var = "hello!"

# A global scope function!
def foo():
    print(my_var)

foo()

''' OUTPUT
hello!
'''
```
Any statements written outside of any blocks - that is no indentation - are said to be 'global' and will be accessible from anywhere in the program. See how we are still able to reference the global variable "my_var" from inside a function block. 

That function 'foo' is also global, so we can call it from anywhere in the program.
``` py
# Later in the same program
def bar():
    print("inside 'bar':")
    foo()

bar()

''' OUTPUT
Inside 'bar':
hello!
'''
```

Now let's look at another example. We're doing to define a new function, and we're going to decare a new variable inside it. Watch what happens if we try to reference that variable outside the function.
``` py
def bazz():
    bazz_var = "Hello from bazz!"
    print(bazz_var)

bazz()
print(bazz_var)

''' OUTPUT
Hello from bazz!
Traceback (most recent call last):
  File "c:\Users\PAL\learn_python\scope.py", line 8, in <module>
    print(bazz_var)
          ^^^^^^^^

NameError: name 'bazz_var' is not defined
'''
```
We get an error telling us that 'bazz_var' is not defined. But surely it must be? We declared it earlier, and we were able to reference it again at least once inside the function okay *[highlight the printed line in the output, before the error, as it might be easy to miss]*, why is it now a problem?

This is because 'bazz_var' is not global. We defined it in bazz, which means we can only use it in bazz. It's a 'local' variable. Once the program exits, or 'returns', out of a function, all local variables are cleared from memory. The program sort of 'forgets' them, because it assumes they're no longer needed.

By the time the program we just looked at gets to line 8 - the problem line - 'bazz_var' is gone. It only ever existed inside bazz.

So why does Python do this? Well, there are a few reasons. The main one is to save space and stop programs taking up too much memory when they run. All those variables and function definitions DO NEED to be stored somewhere. As programs can grow to be very large, with potentially hundreds of functions and thousands of variables, can you imagine if the computer had to hold onto all of them at once? Much better to only load them when they're needed, and clear them away once they're not.

The second is neatness. variables being local to the scope of a function means that multiple variables in different scopes can share the same name, without having to worry about one overriding the other. It also just encourages good practice when designing and writing your code.

## Global vs Local
Take a look at this:
``` py
store = "fizz"
def update_store(new_val):
    store = new_val
update_store("buzz")
print(store)

''' OUTPUT
fizz
'''
```
You might have been expecting it to print out 'buzz', after all, we called the function 'update_store' the change the value of our variable to buzz, why is it now back to fizz again?

Sure if we removed that top line, 'store' would be a local variable and we'd get an error if we tried to reference it out of scope. But surely as 'store' is global, it should be fine? Well, no. You can access variables from a higher scope, and you can do certain operations to alter them (like adding elements to a list) but what you can't do is completely redefine or replace them.

This means that for immutable data types (like strings, booleans, and numbers), we cannot change their values.

We can try, we won't get an error, but it will be treaded like a new variable in memory; a new variable which will eventually be cleared away in favour of the old one.
*[highlight above scopes, annotate variable names with 'new' and 'original' score]*
So far as the computer is concerned, we've defined a completely new, local variable. One which coincidentally shares the name as a global one. But it's not the same.

But what if we need to replace a global variable at the local level? Well generally speaking we don't. If a function is intended to override a variable, its more common to have it return that value, so it can be assigned at the right scope.
``` py
x = 1
def add_one(y):
    y = y + 1
    return y
x = add_one(x)
print(x)
```
But, if we really *really* want to we can use the `global` keyword. This specifies that we're interested in the global property of that name, OR forces that property up to global scope if it wasn't already.
``` py
x = 1

def x_and_y():
    global x
    global y
    x = x + 1
    y = 3

x_and_y()

print(x)
print(y)
```
Although, overusing this feature, or really using it at all if it isn't absolutely necessary, is generally considered a bad habit as it can lead to some pretty messy code. By all means have a play around with it to see how it works, but try not to rely on it.

## What about if, else, and loops?
Do flow-control statements have their own local scopes, too? After all, they use code blocks just like function definitions.

Well, actually no. In some languages, like java...
``` java
if (1 + 2 == 3) {
    String ohNo = "Oh no! This won't work!"
}
System.out.println(ohNo)
```
... this is the case, but Python only scopes objects inside functions and classes. 
``` py
if 1 + 2 == 3:
    phew = "Phew, that worked!"

print(phew)
```

But a lot of time it's a good idea to write your code as if they do. Remember that the whole point of flow-control statements like if is that they're flexible. They can run as you need, as many times as you want, or even not at all. If your 'if' statement is meant do define some important variable you need to reference later, and that if statement ends up not running, you're stuck!
``` py
if 2 + 2 == 5:
    uh_oh = "Uh oh! Not again!"

print(uh_oh)
'''
Traceback (most recent call last):
  File "c:\Users\PAL\learn_python\scope.py", line 6, in <module>
    print(uh_oh)
          ^^^^^
NameError: name 'uh_oh' is not defined
'''
```
Better define them before, with some placeholder or default value, just in case.
``` py
aah = ""
if 2 + 2 == 5:
    aah = "Aah, much better!"

print(aah)
```

## Summary
This all works the way it does to help program scale better as they get larger and start taking up more memory. Understanding scope is vital to making sure your code will behave the way you expect it.

Ideally, if we've designed our code right, scope should never be a problem - but of course even the most experienced of us get caught out occasionally! But the more practice we get, the better!  

