# Primitive data types
Programs, and programming languages, need to somehow encode information at the low level to represent different kinds of things to us at the high level. How is a number `10` different from a name `"Jimmy"`. To us - the human observer - they're obviously fundamental different things: with a number we can count up to it, or down from it, or do all sorts of crazy maths; a name we can read, or write, or swap the letters around, or search through an article for.

But remember what we said about computers in our very first session: smart, but extremely stupid and stubborn. If we want a program that includes both, we need to somehow account for the differences between them. This is where data types come in.

## Strings
Remember when we ran our very first print statement, "Hello, World!", how we enclosed our message in quotation marks. This is the syntax we use to represent strings.

Strings are quite simply: text. whether a single character, or an entire novel - they can be any length. They are most often used for human-readable information such as a name or a message, but can also be used for more abstract or formatted information such as email addresses or phone numbers.

Anything in speech marks will be interpreted by Python as one string. Important to note that, unlike brackets for mathematical and boolean expressions, quotations marks cannot be nested - there are no 'strings within strings' - just one at the beginning and one at the end.

~~~py
message = "In Python, strings are easy!"
~~~
If you need to include quotations marks in the string itself, you can preface each one with backslash. This is what we call and "escaped character"

``` py
message = "\"wow\", he said. \"That's so simple!\""
```

alternatively, you can replace the outer speech-marks with a pair of apostrophes.

``` py
message = '"wow", he said. "That\'s so simple!"'
```

Just be aware that THEN you'll need to escape any internal apostrophes!

In Python, strings can have pretty much any characters you want:
* "UPPER CASE"
* "lower case"
* "123 numbers"
* "Punctuation?! (and spaces)"
and literally thousands of other including alphabets from several languages and many mathematical, scientific, even musical symbols. They can even encode special characters such as linebreaks (that is, the new line when you press enter) and tab indents with their own special characters.
* "that is \n and \t respectively"

An important trick with strings is concatenation, which means to attach two strings together. In Python we can use addition to 'add' two strings:

``` py
message = "Hello, " + "World!"
```

Only we're not really adding them at all. A plus sign between two strings (and they do BOTH need to be strings) denotes concatenation - the two strings will be joined together:

``` py
message = "Hello, " + "World!"
print(message)
```

## Numbers: integers vs floats
Next a quick review of numbers. Storing numbers in Python was one of the very first things we looked at so it should already seem familiar. When we need a number, we just write one
* my_number = 1
with a decimal point if we need it
* my_number = 1.5

Except that Python actually has two data types for representing numbers! The first is integers: integers are strictly whole numbers (including negatives and zero) which can be as large or as small as you need them to be, but strictly NO decimals. 1 is an integer, -1 is an integer, 1.1 is not.

Float are, well, everything else. That is decimals, fractions, even special numbers like pi or infinity. You can encode 2.5, -100.1, 7/11, even the square root of 3975 using floats. This even includes numbers which we would think of as being whole, like 1.0, 2.0 etc.

So does that mean all integers are also floats, but only some floats are integers? Well... kind of... but not really. That is a true statement to make about numbers in the real world, but that's not how Python sees it. In Python, a data object can only be one type or another. if we write this:
~~~ py
num = 1
type(num)
~~~
Python will see 'num' as an integer, but if we write this
~~~ py
num = 1.0
type(num)
~~~
Python will see it as a float, it all depends on how we initially define it.

Worth noting is that we can still use all the same mathematical operators on both, Python will even convert integers to floats when we need to (for instance when division leaves us with a decimal). Any yes, this includes equality, so `1.0 == 1` will be true. *[SIDENOTE: if you want them to be EXACTLY the same you can use the is keyword. `1 is 1` is true, but `1.0 is 1` is false]*

## Booleans
Next, let's recap booleans. Booleans are their own data type in Python, IE either true or false - which In python, we write as the english words 'True' and 'False' with a capital T and F respectively. Also, any boolean expressions, which remember ultimately evaluate to either true or false, are included in the boolean data type. That's really all there is to say.

``` py
bool_f = False
bool_t = True
```

## A quick word about None
One last big important data type we haven't discussed yet is None.

None is nothing.

*[If it's not too "unprofessional", I would love a fake-out cut to the next section here...!]*
Okay no let's explain that in a bit more detail!

None is a value with it's own data type: the None type. None is used to encoded the absence of data. Surely we could already do that with 0 or 'False', but no! 0 is still an integer with a definite value *[SIDENOTE: or 0.0 for a float]*, the empty string is still a string, and false is still the boolean false and not true!

We still need a way to represent data that just isn't there or hasn't been defined yet. This is quite often used is data collections (which we're going to learn about next time) to represent empty or missing values:

```py
cookie_recipe = ["get some flour", None, None, "..?", "cookies!"]
```

## Implicit casting and operators
These are four of the most important data types in Python. To recap:
* Strings
* Integers
* Floats
* Booleans

As you can probably imagine, we have to use certain data types for certain things, for example only numeric data types (ints and floats) can be used for mathematical expressions. However this does not mean that we can never convert between types: converting something from one data-type to another is called *casting*.

Python does a lot of casting automatically, a good example of this division between integers, which we already discussed, which gives us a float:

~~~ py
num1 = 5
num2 = num1 / 2
print(type(num1))
print(type(num2))
~~~ 

print itself is actually another very good example. Technically, print only works with strings, which means anything else has to be casted to a string before it can be printed. Lucky for us, Python does this automatically.

~~~ py
print(2.5)
print(False)
~~~ 

This kind of automatic type conversion is called 'implicit casting'

Explicit casting is when WE, the programmer, TELL the program we want to convert from one data-type to another. We do this by calling the name of the type we want to convert to as a function, and passing in brackets the value with whatever we want to convert from.

~~~ py
int("1")
string(10)
~~~ 

Worth noting is that you can't necessarily cast from anything into anything else, it depends on the types and the data. You can convert any number into a string easily, but not every sting can be converted into a number. Attempting to convert data of one type to another where no such casted value exists gives us an error:

~~~ py
int("one")
~~~

## Summary
Understanding data-types is an essential part of learning programming. It helps us better understand how the program "thinks", or perhaps more accurately how it doesn't, and how everything it DOES do needs to follow some kind of logic. It is out of these base data types we build more complex data structures, and use them in programs of our own. With this in mind, we're ready to start exploring the rest of what programming has to offer.  



# Basic data structures
When we finished off last time we hinted at how we can "build more complex data structures" from the basic types we covered last time.that's exactly what we'll be doing today. Let's get straight into it.

## Lists
In every day speech, a 'list' means a sequence of something, anything, all written down in the same place for convenience. This is pretty much exactly what list means in programming, too. In Python, a list is declared using square brackets, like this:

```py
my_list = []
```

inside those brackets we write the elements, or items, we want, separated by commas:

```py
my_list  = ["bread", "milk", "apples", "eggs"]
```

Those items can be pretty much whatever we want them to be: strings, floats, integers, booleans - we can even mix and match different data types in the same list. We can define elements as literal values, using expressions, or even with variables.

Important to know is that lists are ordered, they're not just a jumbled set of elements! Each item comes after one item, and before another one (with the obvious exception of the start and end of the list). 

We access individual elements of a list like this
~~~ py
print(my_list[0])
print(my_list[1])
print(my_list[2])
~~~ 
That is, the name of the list followed by square brackets containing the number of the element we want. We call this number the index. Note that in Python the index starts at 0; so what we might think of as the 1st element is stored at the 0th index, the 2nd at the 1st index, and so on.

We can also use this syntax to redefine elements in a list:
~~~ py
my_list[0] = "cereal"
print(my_list)
~~~ 
What we can't do is reference an item number that doesn't exist, or an "index out of bounds" as Python will call it in the error message you'll get if you try.
~~~ py
# remember idx 4 would be the 5th element, 
# and the 5th element doesn't exist, 
# there are only 4!
print(my_list[4])
~~~ 

We can add items to the end of a list using `.append()`, or insert them at a specific point using `.insert()` which will shift everything afterwards up an index.
~~~ py
my_list.append("orange juice")
my_list.insert(1, "coffee")
print(my_list)
~~~ 
We can also remove elements of a certain value using `.remove()` or at a specific index using `.pop()`
~~~ py
my_list.remove("eggs")
my_list.pop(0)
print(my_list)
~~~ 
These are examples of list methods. There are actually more than this, but these are four of the most important. You'll easily be able to find all of them by looking at online documentation *[SIDENOTE: "Documentation" - something that tells you how to use the language you're writing in, and what methods do what - like an instruction manual]*. 

Lists are our first example of a 'collection' data type, IE one used to store multiple items of data, and we're about to meet a few more.

## Dictionaries
Next up is dictionaries, another collection data type. Again think what the word dictionary means in common English: with a dictionary, you look up a word, and find that word's meaning:
*[YOU: what is "python"?, DICT: "NOUN: a type of snake found in Africa, Asia, and Australia"]*
*[YOU: what is "recursion"?, DICT: "NOUN: recursion is recursion"]*
In computer science, we call this "mapping", that is the idea that one value points - is mapped to - another. We call this fist value the 'key', and the other the 'value'. A bit like a chart, or map legend, or - well - a dictionary!
*[annotate/highlight dictionary examples with KEY for words and VALUE for definition]*
Python's in-built dictionaries implement this mapping, that is they allow you to store and retrieve key-value pairs.

In Python we can declare an empty dictionary like this:

```py
my_dict = dict()
```

Let's see how it works with a simple example, by mapping people by their names to their favorite colour. Dictionary items use a very similar syntax *[REFRESHER - syntax: the way code needs to be written in a certain language]* to lists, that is: the name of the dictionary followed by square brackets.

```py
my_dict[]
```

Only, instead of an index number (like for lists) it is in these square brackets we write our key. We then define it (that is, assign a value to the key) as whatever we want.

```py
my_dict["alice"] = "blue"
```
we access the value in much the same way.

```py
print(my_dict["alice"])
```
Let's add a few more:
~~~ py
my_dict["bob"] = "red"
my_dict["charlie"] = "yellow"
my_dict["dio"] = "red"
~~~
This raises an important point. We ARE allowed duplicate values, that is two separate keys pointing to the same value - see how Dio *[It was me, Dio!]* and and Bob both have the same favorite colour, "red".
*[maybe the classic map diagram, keys on left values on right arrows in between. Both Dio and Bob pointing to red]*
What we cannot do is have two values assigned to the same key, that is one key pointing to two things at once. If we try this in Python:
~~~ py
my_dict["dio"] = "blue"
print(my_dict["dio"])
~~~
you'll see that we only end up replacing the original value.

Maybe now you have a question: "surely that's not like a dictionary at all, with a dictionary a word can have more than one meaning". Say "rock", which can either be a big lump of mineral, or a type of music. Unfortunately, in Python we can't do this; but we can fake it.

A key can only have one value, but that value can be a collection - with multiple items inside it. If Charlie has two favorite colours, we can assign their value as a list:
~~~ py
my_dict["charlie"] = ["yellow", "pink"]
print(my_dict["charlie"])
~~~
And yes, if you were curious, you can have a value in a dictionary be another dictionary. In fact you can pretty much nest any data collections you want: you can have lists of lists, dictionaries of lists, lists of lists of dictionaries of lists. etc. Just keep in mind that it can get messy, very quickly.

Dictionaries, like lists, and like all data types in fact, have several built in methods to make working with them easier. We won't be going over them all - and you'd be unlikely to use them all in a single program - but we recommend taking a look at them: they're easy to find documentation for online.

## A brief pause
Dictionaries and lists are by far the most commonly used data collection in python, and thus the two most important to understand - hence why we went over them in as much detail as we did. But there are still two more types built into Python, with their own special syntax. While not used as much, they ARE still important, and both have cases where they are the best (or even only) choice.

Thankfully, once we do understand lists and dictionaries, the remaining two can be explained pretty simply. We're going to go over them briefly.

## Sets
Sets are actually very simple: they're like lists, but they're completely unordered. Sets really ARE like a jumbled bag of items. They also can't have duplicate items, an item is included once, or not at all. In Python, sets are written with curly brackets.
``` py
primes = {2, 3, 5, 7}
```
You might be thinking "if they're un ordered, how to we access specific elements of a set?". And, well, you don't...

you can add items, remove items, get all or some of the items at random. But you can't pick, say, the first one because there IS no first one. They're all mixed together.

## Tuples
Tuples, also very similar to lists, are written with round brackets, and comma separated items, and accessed with the index number in square brackets.
``` py
full_name = ('john', 'william', 'smith')
print(full_name[0])
```
The big difference with tuples, is that once they're defined, you cannot add or remove any elements to them; they're like lists that get locked shut as soon as you define them. You can't replace any items either, if you try:
``` py
full_name[1] = 'alan'
```
you get an error.

You can change the elements without completely overriding them, if that's possible (which depends on what kind of data type the elements are). For example you can do this:
``` py
l1 = [1, 2]
l2 = [4, 5]
t = (l1, l2)
t[0].append(3)
print(t)
```
but not this:
``` py
l1 = [1, 2]
l2 = [4, 5]
t = (l1, l2)
l1 = [1, 2, 3]
print(t)
```

## Summary
Data structures like these allow our program to be a lot more flexible. They also introduce organization which is essential for many different algorithms, and is also just nice to have for us. It can be a lot easier to visualize one variable with a list of 10 things, all in a set order, than 10 different variables with different names and no way to order them. Although of course which is actually better always depends on the problem you're trying to solve.

Not only is learning these data structures important for learning programming, but observing how they build off the fundamental data types, and how in turn we could see more complex functionality emerging by using *them*, is exactly the kind of logic that will serve us well not just int learning *to* code, but in coding itself.