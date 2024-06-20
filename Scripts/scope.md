# A quick word on scope
This topic will be a brief one, as there's not too much to cover, but it's both:
* an important enough topic that it is essential to understand
* a general enough topic that it wouldn't make sense to squeeze it in anywhere else - it deserves it's own video.
We are of course talking about scope.
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
By now we should have looked at flow of control statements - that is our if, elifs, elses, and loops. We will have also taken our first look at functions, and how we define them. This means we should be comfortable with the idea of code blocks.
``` py
# Old block, boring
my_bool = True

if my_bool:
    # New block, exiting!
    print("Wow, blocks are so exciting!")

# Back to the old block...
my_bool = false
```
We know that blocks are the ways we separate out lines of code into groups - which is essential for things like flow-control statements to work, otherwise we wouldn't know which lines were part of a statement's body and which were just at the base level.

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

# What is scope?
Put very simply, scope means anything your program stores for later, like variables or function definitions, it only keeps for as long as your program stays in a given block.

But it is best explained with an example:
``` py
store = "fizz"
if store == "fizz":
    store = "buzz"
print(store)
```
What do you think this program will print? It's not a trick question: the answer is "buzz". *[running through the code]* We declare a variable, our 'store' at the start, we then enter into a new block (the body of an if statement) where that variable gets redefined. When we print it out, this variable still has it's new value.

Let's change the code a bit:
``` py
store = "fizz"
def update_store(new_val):
    store = new_val
update_store("buzz")
print(store)
```
See now we've introduced a function, 'update_var' which takes one argument, and assigns that argument to the variable store. Now what happens?

*[surprise, it's still "fizz"!]*

Now it says that store is still fizz? How can that be, didn't we change it to be buzz? Well yes and no. You see, this is a prime example of variable scope in action.

By the end of this session, we're going to explain why this happened, but first let's look at it from another angle. Say we didn't define store at the start at all, and only defined it in the function:
``` py
def update_store(new_val):
    store = new_val
update_store("buzz")
print(store)
```
You'll see that this time, no only do we not get to see "buzz" printed out, we get an error!
```
File "c:\Users\PAL\learn_python\scope.py", line 4, in <module>
print(store)
      ^^^^^
NameError: name 'store' is not defined
```
It's telling us that that store 'is not defined', which is the same error message we get when we try and access a variable that doesn't exist. But surely 'store' DOES exist, we defined it in our function!

But that's just the thing, we defined it in our function AND ONLY our function - not outside. This means that 'store' will be local. As soon as we leave that block in runtime, Python sort of 'forgets' that variable - it assumes it will no longer be needed and clears it from memory.

We call the space in which that variable still exists it's 'scope'. *[highlight scope of 'store' in above example]*.

## How does it work?
In Python, the scope of any object definition (that is functions, variables and *classes* - which we'll get to later) is determined by which block it first appears in. This is easiest to see at the base level:
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
Any statements written outside of any blocks - that is no indentation - are said to be 'global' and will be accessible from anywhere in the program. See how we are still able to reference the global variable "my_var" from inside a function block. That function 'foo' will also be global, meaning we can reference it later even from inside a new function definition.
``` py
# Later in the same program
def bar():
    other_var = "Inside 'bar':"
    print(other_var)
    foo()

bar()

''' OUTPUT
Inside 'bar':
hello!
'''
```
See how now we've defined a second variable, 'other_var'. This variable is NOT global, it is defined for the first time inside bar - we say that it is 'local' to bar. But of course, we can still use it inside that function like we've done here, passing it to a print statement.



We can only reference variables that are in-scope. If we try and reference any variables that have fallen out of scope, that is the program has moved on from whichever block they were first defined in, it's like they never existed.

## Some more examples
See this code:
```py
x = 2
y = 3
def foo():
    y = x + y
    print(x)
    print(y)
    print("added:")
print(z)

'''
2
3
added:
Traceback (most recent call last):
  File "c:\Users\PAL\learn_python\scope.py", line 9, in <module>
    print(z)
          ^
NameError: name 'z' is not defined
'''
```
You'll se that when we run this we, of course, get an 'is not defined' error. As you may have spotted, this is because we tried to reference the variable 'z' at the top-most, or 'global' scope, when we only define it in the scope of function 'foo'.

But not before that function runs, and successfully accesses the variables x and y which ARE defined at the global scope. Remember that scopes, like the block's they've tied to, are nested.
*[Highlight different scopes in different coloured overlays, along with which variables they have]*
Worth noting is that functions are also included in scopes, so here the function 'foo' is part of the global scope.

Let's go back to our example from earlier.
``` py
store = "fizz"
def update_store(new_val):
    store = new_val
update_store("buzz")
print(store)
```
We know why this wouldn't work if we remove the top line, but surely as 'store' is part of the global scope, it should be fine? Well, no. You can access variables from a higher scope, and you can do certain operations to alter them (like adding elements to a list) but what you can't do is completely redefine or replace them.

We can try, we won't get an error, but it will be treaded like a new variable in memory; a new variable which will eventually 'fall out' of scope in favour of the old one.
*[highlight above scopes, annotate variable names with 'new' and 'original' score]*

But what if we need to? Well generally speaking we don't, if a function is intended to override a variable, its more common to have it return that value, so it can be assigned at the right scope.
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
    y = x + 1

x_and_y()

print(x)
print(y)
```
Although, overusing this feature, or really using it at all if it isn't absolutely necessary, is generally considered a bad habit as it can lead to some pretty messy code. By all means have a play around with it to see how it works, but try not to rely on it.

## Summary
Understanding scope is vital to making sure your code will behave the way you expect it. Scope works the way it does to help program scale better as they get larger and start taking up more memory - it also serves to allow and encourage better practices when programming.

Remember that in Python, scope is determined by the blocks of functions and classes (which we'll get to later). Ideally, if you've designed your code right, scope should never be a problem - but of course even the most experienced of us get caught out occasionally! But the more practice you get, the better!  

