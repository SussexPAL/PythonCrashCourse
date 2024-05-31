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

It's very easy to define variables in Python, we just give it a name and then define what we want it to be using the equals symbol and some value on the right.

`my_number = 5`

It's worth noting that variable names in Python cannot have spaces. If we want more than one word, we usually separate them using an underscore (like we've done here). Now we can then use this variable anywhere we want to refer back to whatever value we defined it as.

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

`my_number = 1 + 1`
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

## Basic maths operators - "the big four"
We already looked at the plus operator last time, let's introduce a few more and round out the "big four" of maths operators: *[symbols written/appear, but with the traditional symbols (x, ÷) for multiplication and division as we'll explicitly 'correct' them in a moment]* 
* Addition
* Subtraction
* Multiplication
* Division

### Subtraction
Starting with subtraction *[zooming in/focusing/whatever on the symbol]*, we have the standard dash, which works pretty much exactly how you'd expect it to: much like for addition, we put it in between two numbers (or number expressions, or variables) remembering the space on either side, where the second number is subtracted for the first. Simple.

*[some examples]*
`my_var = 10 - 9`
`my_other_var = 5 - 1 - 2`
`my_negative_var = 0 - 1`

We use this same symbol to indicate negative values, as well! Only this time, *no space!* we put the symbol immediately before the value, and it becomes negative. Or, a positive if the original value would be negative, remember the rule of double-negatives!

`my_negative_var = -1`
`my_other_negative_var = -my_other_var`
`double_negative = -my_negative_var`

### Multiplication
Next multiplication. You may be used to seeing this symbol used for notification: `thing = 2 x 2`, this 'x' right here. But most programming languages don't use this, what if we had a variable called 'x'? how would the program know which one we were talking about? Instead we use this `thing = 2 * 2` *[cross out and replace 'x' symbol on original list of operation symbols]* asterisk instead. Most keyboards, including standard QWERTY ones, will have this on the 8 key. Beyond that there's no surprises, again this is an *infix* operator, so it goes *between* two values.

`x = 12 * 3`
`y = 1 * 1 * 1`
`z = 2 * y`

### Division
Maybe you're used to seeing this symbol for division `thing = 2 ÷ 2`. Just like our last operator, this isn't the symbol used in most programming languages (including Python), but unlike multiplication this isn't done out of fear of confusion, just that most keyboards don't *have* a key for the division sign. Instead we use a simple forward slash `thing = 2 / 2` *[as above, replace '÷' symbol]*, meant to resemble fractions (which, after all, is division). let's see it in action:

`it_in_action = 5 / 2`
`print(it_in_action)`

This raises a good point: Python DOES support decimal numbers, and they're written according to convention with a dot (period/full stop) to mark the decimal place. Doing division quite often leaves us with decimal numbers. Although, if you are familiar with division by remainder, we'll look at that in just a moment.

## Further maths operators
We've seen the big four, let's look at some more!
* modular division
* Powers
* Brackets (parenthesis) *[Yes I know this isn't an operator leave me alone]*

### Modular division
We just looked at division, where we divided out first value, the *dividend*, by the second, the *divisor* to get some answer *[show example equation `ans = 3 / 2`, with key terms and answer added]*. We also know that this is full division, so if our divisor is not a multiple of our dividend, then our answer will not be a whole number *[highlight that ans = 1.5]*, because the second value does not 'fit into' the first a whole amount of times without some remainder.

But what if it's exactly that remainder that we care about? This is when we use modular division, `quotient = 3 % 2` for which we use the percentage symbol (found on most keyboards on the 5 key), this will give us the value of the remainder (called the quotient) when the dividend is divided by the divisor.

Don't get confused, this is NOT the same as doing full division, and then rounding down if we end up with a decimal *[show `11 % 2` = 5 with a big red line through it. Side note: we CAN do this with a double slash '//']*. Modular division gives us the quotient (the remainder) and ONLY the quotient. *[`11 % 2` = 1 with a big tick!]*. If we do modular division where the divisor IS a multiple of the dividend (IE when full division would give us a whole number) then the quotient will be 0 *[`10 / 2` = 5, `10 % 2` = 0]*

*[maybe talk about how we can use this to see if a number is odd/even by doing `x % 2`, idk if this bit is too long already...]*

### Powers
Next up is powers. If you're unfamiliar, a power is when we take a number and multiply it by itself a certain number of times. This is most commonly seen in squaring (the power of 2) and cubing (the power of 3) *[examples of 2 squared and 2 cubed, with workings]* but we can raise a number to the power of any number we want *[examples of 2 to the power of 2, 100, and 1]*. We can EVEN use zero, negatives, and decimals! *[examples of 2 to the power of 0, -2, and 25 to the power 0.5]* Although exactly how these are worked out goes a little beyond the scope of this topic, just know that Python can do it! 

To do this we use a double asterisk `2 ** 2` between two numbers, where the first number (the base) is raised to the power of the second number (the exponent)

### Brackets (parenthesis) 
While not technically an operator, now is a good time to talk about brackets. In python, we can add brackets to an expression to explicitly state the order of operation. If you're familiar with BIDMAS, Python follows the exact same rules. If not, remember that Python will evaluate expressions in brackets FIRST, then (if there are any) powers, then division and multiplication, then addition and subtraction. *[show expression `(1 + 1)**2 / 2 + 1` being evaluated step by step]*

Here are some examples where adding brackets is important:
`a1 = 2 * 2 + 1`
`a2 = 2 * (2 + 1)`
`b1 = 2 ** 1 + 1`
`b2 = 2 ** (1 + 1)`

Remember that any expression IN brackets still follows the same rules of order of evaluation. If we need to, we can nest brackets (brackets within brackets) just remember to make sure they're balanced!

`c1 = 2 * (2 / 1 + 1)`
`c1 = 2 * (2 / (1 + 1))`

# Video 3 : Boolean logic and operators
*[title card]*
Okay, by now we've seen how we can do maths on Python, and how variables and expressions work. We're now going to introduce the idea of boolean logic. This may feel a bit more like a leap into the abstract; compared to the simple numeric and mathematical logic we've been looking at, which everyone will have seen in their life before, boolean logic is a little more specific to computer science, and so it may or may not seem quite as familiar. But that doesn't mean it's complicated - it can actually be put very simply.

A boolean can be only one of two things: *[some graphic here]* true, or false. No numbers, no in-betweens or maybes here - this is *binary* logic. A boolean expression is structured in much the same way as a maths expression *[show two expressions: (10 / 5) and (10 > 5)]*, only while a maths expression is evaluated down to a number, a boolean expression is evaluated to be either true of false *[previous expressions collapse to 2 and true respectively]*.

Let's lake a look at our first couple of example:
`1 + 1 == 2`
`2 + 2 == 5`

* Equality
* Inequality
* Less than/greater than
* Less than/greater than or equal
* NOT, OR, and AND keywords