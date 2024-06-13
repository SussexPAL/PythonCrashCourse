# Further functions
By now we should have already seen how the basics on functions work - we know that functions can take arguments (or parameters), and give us some return value back. We also know how to define our own functions - what parameters we want them to take, and how we get them to return values.

These are actually all the fundamentals that we need to know, but that doesn't mean there's no more to talk about. In this session we'll be looking at some of the more advanced use cases of functions, as well as some of the handy tricks that python has built in to make working with functions easier.

[SIDE CAM]
## Key word arguments
Remember from last time that we define function parameters in the brackets of our function signature. *[SIDE NOTE: The first line of a function definition, ie `def foo(x, y, z) is called the signature]* We said we had to give them valid and unique names...
```py
def some_function(num1, num2):
    return num1 + (num2 * 2)
```
For this example, this means every call of this function must be given 2 arguments - num1 and num2 in that order.
```py
# The order is important!!
val1 = some_function(4, 5)
val2 = some_function(5, 4)

print(val1)
print(val2)
```

This is great and for most applications it's enough - but it's not very flexible. What if we want the function to be able to run 

## Type hints
Look at this function signature
``` py
def my_function(something):
    # ...
```
Here's a fu

## Internal functions

## Introducing recursion

## Summary
