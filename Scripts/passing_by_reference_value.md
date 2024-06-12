# Reference vs Value
Before moving on, we're going to take a brief moment to break down the concept of arguments and variables as references, vs as values. If these aren't phrases you've heard before, don't worry: this is a topic we've hinted at before but have avoided explaining in full because it wasn't essential to understand at that point. 

By now though, you should have been introduced to the idea of OO programming, meaning that the difference between passing by reference and passing by value is no longer something we can gloss over.

Thankfully, it doesn't take to long to explain. But like many new ideas, it may seem a bit hard to take in at first - that's okay, to be expected even. That is the entire point of learning a new skill: not to grasp it instantly, but to gradually build up an understanding over a period of time until it feels like second nature.

Just like the others, you can review this section as many times as you need to.

Let's get started.

## Passing by value
[SIDE CAM/CUT AWAY]
Take a look at this.
```py
def foo(x: int):
    # Takes a number x and adds 1 to it
    # does not return anything
    x = x + 1

y = 10

foo(y)

print(y)
```
What number do you think this program will print?

We have some variable y that gets passed to a call of function foo - 'foo' takes that variable and adds one to it. As y starts with a value of 10 and then gets passed to foo - so then, the program should terminate with y = 11. 

On the other hand, knowing what we know about how functions work, surely when foo is called y's value is passed to x. x only exists in the scope of the function, and it's x that gets increased from 10 to 11, not y. "What happens in foo, stays in foo", there's no return statement, and y itself never changes, so y = 10... right?

Both are reasonable guesses, but surely it can only be one or the other? Let's run it and see what actually happens...
*[we run the program, surprise: it's 10!]*
It's 10! The value of 'y' stays at 10 even after it's passed through 'foo'. If this wasn't what you were expecting, let's take a second to break it down:

[CENTER CAM]
Variable 'y' contains the number 10. When y is given as an argument to 'foo', it is that number 10 which is passed into the body of the function, and not the variable 'y' itself. We call this 'passing by value', so called because it is the VALUE and ONLY the value which is given to the function. 

The inside of the function call only sees the number 10. It doesn't know whether it got that from:
* a variable *[y = 10 \n foo(y)]*
* a literal number *[foo(10) ]*
* or some other expression *[foo(5 + 5)]*
and it doesn't really care. 10 is 10, after all.

This is because of how numbers are handled in the background by Python. Numbers are "immutable", they never change. We can move from one number to another, but each number itself is fixed. Think of it this way, if we just passed the value 10 directly...
`foo(10)`
`print(10)`
... we wouldn't expect this code to somehow change to the value of 10 so that `10 == 11`, that would be impossible, 10 is always 10 and 11 is always 11.
`y = 10`
`foo(y)`
`print(y)`

## Passing by reference
[SIDE CAM/CUT AWAY]
All that in mind, let's look at the following.
```py
class NumBox:
    # This class is just a simple 'wrapper' for a single number, stored as a field
    def __init__(self, num):
        self.num = num

def bar(x: NumBox):
    # Takes a NumBox object x and adds 1 to its num property
    # does not return anything
    x.num = x.num + 1

a = NumBox(10)
bar(a)
print(a.num)
```
Here we've defined a new, but very simple class, which we've called NumBox. See NumBox has only property, the number 'num' which is defined at the constructor. *[SIDE NOTE: A class that contains one thing like this is called a 'wrapper'!]*

Our function bar takes a NumBox object and increases it's number property by one. Just like foo in our last example, it doesn't return anything, only modifying it's parameters.

[CENTER CAM]
Knowing what we know, we expect the printed value to be 10. Our variable a is defined as a NumBox object with a num of 10 - a is then passed to a call of function `bar`. We expect that when bar receives that parameter as argument x, it treats is as a new object - sort of a copy of the original one if you like. Only this copy gets changed, so the original stays the same...

... right?

*[show code output. it's 10!]*
Except, no - surprise! - it was a trick question. But why, doesn't that contradict what we said happened in our first example? Well, this time things are different.

Remember we said that integers were passed by value because they were imitable, that is they never change - 10 is 10, 11 is 11, and they always will be. Objects, of any class no mater how simple, are different - they are mutable: they're not constant, they can change, in fact most of them are changing all the time.

This means, when given as arguments, they are passed by NAME - that is instead of an identical copy, Python actually SHARES the original object with the function. Any changes it makes WILL AFFECT the original object. The reason it's called passing by name is because what the function actually receives is a POINTER to the original object, sort of like a name tag that tells it where to find it.

## But... why...?
Before diving into the nuts and bolts of why this works the way it does - let's recap, as well as give a handy sort of "cheat sheet" overview you can come back to.

If a function takes an argument, that argument has to be passed to it.

For items that are passed by value: the function receives a copy of the original with an identical value. It can change this copy, but the original stays the same.

For items that are passed by name: the object is not copied across, but instead shared with the function. What the function receives a pointer, if it changes the object by this pointer - it is changing the original object.

[SIDE CAM]
*[list on screen would be good]*
The objects Python passes by value are you primitive data types:
* integers
* floats
* strings
* booleans
The objects that Python passes by name are, well, pretty much everything else:
* lists
* dictionaries
* ... every other data collection type
* any class objects

[CENTER CAM]
So why does it do this? It's got everything to do with said earlier about data being mutable or immutable. Numbers never change - when we add two number together, we're not changing either number, we're working out an entirely new one. The same goes for every other mathematical operator, as well as any operations on strings and booleans.

We can even see this in the syntax. When we increased x, we didn't just change it we completely replaced it.
`x = x + 1`
X now equals something different that it did before - the fact that its new value is based of the old one doesn't no longer matters, the old x is gone!

But if x is an object and we change one of it's properties - then it's different.
`x.num = x.num + 1`
x's '.num' property might have been swapped out - and it HAS been swapped out, 'x.num' is a new number now - but the actual object x remains. We didn't redefine x, just one of it's properties, potentially one of many.

## Summary
With this concept we've taken our first real peak behind the curtain as to how the computer actually handles things in memory. Understanding this kind of low-level logic isn't always essential, it can be very useful.

Passing by name vs value might seem kind of arbitrary now, but the more code we write, the more we'll see why having and understanding this distinction is so important - especially if we want to write programs with complex data structures like our collections and classes.