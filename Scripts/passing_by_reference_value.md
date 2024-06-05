# Further OO programming
By now we should have a fairly robust understanding of how object oriented programming works and how we use it in Python. We're now going to be looking at some more advanced and complicated use cases, focusing on how objects of different classes can interact with each other in the same program.

## Passing by value
But before we do that, there's some groundwork we need to cover. I want you to take a minute to look at the following program:
`def foo(x: int):`
`    # Takes a number x and adds 1 to it`
`    # does not return anything`
`    x = x + 1`

`y = 10`

`foo(y)`

`print(y)`
When run, what number do you think this program will print? You may have guessed 11 or 10: 11 because we are passing the variable y to a function 'foo' which increments whatever it is given by 1, or 10 because 'y' is never explicitly reassigned or altered after its initial definition, outside of the scope of the function foo (where it's given as a parameter)

These are both perfectly reasonable guesses. Let's see what actually happens...
*[we run the program, surprise: it's 10!]*
 It's 10! The value of 'y' stays at 10 even after it's passed through 'foo'. If this wasn't what you were expecting, let's take a second to break it down:

 This is because of how numbers are handled in the background by Python. When a number (that is a float or integer) is passed as an argument into some function or method, it is treated - within the scope of that function - as a separate item. If it is changed on the inside of a function, this change is not reflected outside after that function returns.

 This is because numbers as "immutable", they never change. We can move from one number to another, but each number itself is fixed. Think of it this way, instead of passing 10 as a variable y, what if we just passed the value 10 directly.
`foo(10)`
`print(10)`
We wouldn't expect this code to somehow change to the value of 10 so that `10 == 11`, that would be impossible, 10 is always 10 and 11 is always 11.
`y = 10`
`foo(y)`
`print(y)`
This is no different. Variable 'y' contains the number 10. When y is given as an argument to 'foo', it is the number 10 which is passed into the body of the function, and not the variable 'y' itself. We call this 'passing by value', so called because it is the VALUE of the variable which is passed, and not the variable itself. You can think of it as a new copy of the original argument, separate from the original in memory.

If we wanted y to be 11, we could tweak the code a little to look like this:
 `def foo(x: int):`
`   # Takes a number x and adds 1 to it`
`   # THEN RETURNS x`
`   x = x + 1` *[highlight lines which are different]*
`   return x` *[highlight lines which are different]*

`y = 10`

`y = foo(y)` *[highlight lines which are different]*

`print(y)`
THIS code actually DOES reassign y as 11.

## Passing by reference
All that in mind, let's look at the following.
`class NumBox:`
`    # This class is just a simple 'wrapper' for a single number, stored as a field`
`    def __init__(self, num):`
`        self.num = num`

`def bar(x: NumBox):`
`    # Takes a NumBox object x and adds 1 to its num property`
`    # does not return anything`
`    x.num += 1`

`a = NumBox(10)`
`bar(a)`
`print(a.num)`

