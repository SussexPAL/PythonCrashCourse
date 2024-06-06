# Primitive data types
Programs, and programming languages, need to somehow encode information at the low level to represent different kinds of things to us at the high level. How is a number `10` different from a name `"Jimmy"`. To us - the human - observer, they're obviously fundamental different things: with a number we can count up to it, or down from it, or do all sorts of crazy maths; a name we can read, or write, or swap the letters around, or search through an article for.

But remember what we said about computers in our very first session: smart, but extremely stupid and stubborn. If we want a program that includes both, we need to somehow account for the differences between them. This is where data types come in.

## Strings
Remember when we ran our very first print statement, "Hello, World!", how we enclosed our message in quotation marks. This is the syntax we use to represent strings.

Strings are quite simply: text. whether a single character, or an entire novel - they can be any length. They are most often used for human-readable information such as a name or a message, but can also be used for more abstract or formatted information such as email addresses or phone numbers.

Anything in speech marks will be interpreted by Python as one string. Important to note that, unlike brackets for mathematical and boolean expressions, quotations marks cannot be nested - there are no 'strings within strings' - just one at the beginning and one at the end.

`message = "In Python, strings are easy!"`

If you need to include quotations marks in the string itself, you can preface each one with backslash. This is what we call and "escaped character"

`message = "\"wow\", he said. \"That's so simple!\""`

alternatively, you can replace the outer speech-marks with a pair of apostrophes.

`message = '"wow", he said. "That\'s so simple!"'`

Just be aware that THEN you'll need to escape any internal apostrophes!

In Python, strings can have pretty much any characters you want:
* "UPPER CASE"
* "lower case"
* "123 numbers"
* "Punctuation?! (and spaces)"
and literally thousands of other including alphabets from several languages and many mathematical, scientific, even musical symbols. They even encode special characters such as linebreaks (that is, the new line when you press enter) and tab indents with their own special characters.
* "that is \n and \t respectively"

An important trick with strings is concatenation, which means to attach two strings together. In Python we can still use addition to 'add' two strings:
`message = "Hello, " + "World!"`
Only we're not really adding them at all. A plus sign between two strings (and they do BOTH need to be strings) denotes concatenation - the two strings will be joined together:
`print(message)`

## Numbers: integers vs floats
Next a quick review of numbers. Storing numbers in Python was one of the very first things we looked at so it should already seem familiar. When we need a number, we just write one
* my_number = 1
with a decimal point if we need it
* my_number = 1.5
Except what we *haven't* covered yet, is that whether or not that decimal point is included is important.

Python actually has two data types for representing numbers! The first is integers: integers are strictly whole numbers (including negatives and zero) which can be as large or as small as you need them to be, but strictly NO decimals. 1 is an integer, -1 is an integer, 1.1 is not.

Float are, well, everything else. That is decimals, fractions, even special numbers like pi or infinity. You can encode 2.5, -100.1, 7/11, even the square root of 3975 using floats. This even includes numbers we would think of as being whole, like 1.0, 2.0 etc.

So does that mean all integers are also floats, but only some floats are integers? Well... kind of... but not really. That is a true statement to make about numbers in the real world, but that's not how Python sees it. In Python, a data object can only be one type or another. if we write this:
~~~
num = 1
type(num)
~~~
Python will see 'num' as an integer, but if we write this
~~~
num = 1.0
type(num)
~~~
Python will see it as a float, it all depends on how we initially define it.

Worth noting is that we can still use all the same mathematical operators on both, Python will even convert integers to floats when we need to (for instance when division leaves us with a decimal). Any yes, this includes equality, so `1.0 == 1` will be true. *[SIDENOTE: if you want them to be EXACTLY the same you can use the is keyword. `1 is 1` is true, but `1.0 is 1` is false]*

## Booleans
Lastly, let's recap booleans. Booleans are their own data type in Python, IE either true or false - which In python, we write as the english words 'True' and 'False' with a capital T and F respectively. Also, any boolean expressions, which remember ultimately evaluate to either true or false, are included in the boolean data type. That's really all there is to say.

## Implicit casting and operators
These are four of the most important data types in Python. To recap:
* Strings
* Integers
* Floats
* Booleans

As you can probably imagine, we have to use certain data types for certain things, for example only numeric data types (ints and floats) can be used for mathematical expressions. However this does not mean that we can never convert between types: converting something from one data-type to another is called *casting*.

Python does a lot of casting automatically, a good example of this division between integers, which we already discussed, which gives us a float:
~~~
num1 = 5
num2 = num1 / 2
print(type(num1))
print(type(num2))
~~~
print itself is actually another very good example. Technically, print only works with strings, which means anything else has to be casted to a string before it can be printed. Lucky for us, Python does this automatically.
~~~
print(2.5)
print(False)
~~~
This kind of automatic type conversion is called 'implicit casting'

Explicit casting is when WE, the programmer, TELL the program we want to convert from one data-type to another. We do this by calling the name of the type we want to convert to as a function, and passing in brackets the value with whatever we want to convert from.
~~~
int("1")
string(10)
~~~
Worth noting is that you can't necessarily cast from anything into anything else, it depends on the types and the data. You can convert any number into a string easily, but not every sting can be converted into a number: if we try this `int("one")` we get an error.

# Summary
Understanding data-types is an essential part of learning programming. It helps us better understand how the program "thinks", or perhaps more accurately how it doesn't, and how everything it DOES do needs to follow some kind of logic. It is out of these base data types we build more complex data structures, and use them in programs of our own. With this in mind, we're ready to start exploring the rest of what programming has to offer.  

# Basic data structures
When we finished off last time we hinted at how we can "build more complex data structures" from the basic types we covered last time.that's exactly what we'll be doing today. Let's get straight into it.

## Lists
In every day speech, a 'list' means a sequence of something, anything, all written down in the same place for convenience. This is pretty much exactly what list means, too. In Python, a list is declared using square brackets, like this:
`my_list = []`
inside those brackets we write the elements, or items, we want, separated by commas:
`my_list  = ["bread", "milk", "apples", "eggs"]`
Those items can be pretty much whatever we want them to be: strings, floats, integers, booleans - we can even mix and match different data types in the same list. We can define elements as literal values, using expressions, or even with variables.

Important to know is that lists are ordered, they're not just a jumbled set of elements! Each item comes after one item, and before another one (with the obvious exception of the start and end of the list). 

We access individual elements of a list like this
~~~
print(my_list[0])
print(my_list[1])
print(my_list[2])
~~~
That is, the name of the list followed by square brackets containing the number of the element we want. We call this number the index. Note that in Python the index starts at 0; so what we might think of as the 1st element is stored at the 0th index, the 2nd at the 1st index, and so on.

We can also use this syntax to redefine elements in a list:
~~~
my_list[0] = "cereal"
print(my_list)
~~~
What we can't do is reference an item number that doesn't exist, or an "index out of bounds" as Python will call it in the error message you'll get if you try.
~~~
# remember idx 4 would be the 5th element, and the 5th element doesn't exist, there are only 4!
print(my_list[4])
~~~

We can add items to the end of a list using `.append()`, or insert them at a specific point using `.insert()` which will shift everything afterwards up an index.
~~~
my_list.append("orange juice")
my_list.insert(1, "coffee")
print(my_list)
~~~
We can also remove elements of a certain value using `.remove()` or at a specific index using `.pop()`
~~~
my_list.remove("eggs")
my_list.pop(0)
print(my_list)
~~~
There are actually more list methods (that is 'list.something()') than this, but these are four of the most important. Lists are our first example of a 'collection' data type, IE one used to store multiple items of data, and we're about to meet a few more.

## Dictionaries

## Sets

