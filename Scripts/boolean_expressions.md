# Boolean expressions
By now we should be comfortable with the idea of Boolean expressions - that is statements that are either True or False. We've seen some of the operators we can use to express them, such as equality, inequality, greater-than, less-than etc.
**booleans.png**
``` py
my_var = 100

# These are all boolean expressions being printed!
print(2 + 2 == 4)
print(5 != 6)
print(7 != 7)
print(my_var < 1)
```

We're now going to look at some special logic operators we can use to combine multiple booleans into one expression.

## Boolean logic operators
Let's say we have two booleans, we'll just call them bool_a and bool_b. Say we also have some code we want to run only if BOTH booleans are true. One thing we could do is use a double-nested if statement:
**double-if**
``` py
bool_a = 1 + 1 == 2
bool_b = 2 + 2 == 5

if bool_a:
    if bool_b:
        print("Both are True")
```
And this would work well enough, but there's a much simpler solution. The AND operator.

As the name implies, 'and' is a keyword which binds together two booleans, and gives true only if BOTH are true. Like most of the other operators we've seen, this is an INFIX operator, meaning it goes between two values.
**and**
``` py
if bool_a and bool_b:
    print("Both are True")
else:
    print("At least one was False")
```

Similar is the OR operator - this has it's own keyword, and similarly combines two booleans into one, giving true if AT LEAST one is true. Or, in other words, only giving false if BOTH booleans were false:

**or**
``` py
if bool_a or bool_b:
    print("At least one was True")
else:
    print("Both were false")
```

Last of this little trio is the XOR or 'zor' operator. This one is interesting (and not just xor is fun to say!). Again, it binds two booleans, and this time gives True if one BUT NOT BOTH statements are true.

**xor**
``` py
# We use '^' to XOR booleans
# usually found on the '6' key
if bool_a ^ bool_b:
    print("One is True, one is false")
else:
    print("Either both were false, or both were true")
```

There is also the NOT operator - which inverts a boolean (so true becomes false, false becomes true). This one's a bit different because it only takes one value instead of combining two. It's a PREFIX operator, so you put it BEFORE the value you want to invert.

**not**
``` py
if not a:
    print("a is NOT true!")
```

## Writing complex booleans statements
We can, of course, use multiple of these operators to group together 3, 4, or a hundred different expressions to one boolean value. Keep in mind that by default Python associates these operations to the left.

which means that if we write `a or b and c`, Python interprets that as "a or b - and c":
**a-or-b-and-c**
``` py
if a or b and c:
    print("a is true...")
    print("and so is 'a or b'")
```

But just like mathematical expressions, we can use brackets to explicitly state the order of evaluation - statements in brackets get evaluated first!

**a-or-b-and-c-brackets**
``` py
if a or (b and c):
    print("Either a is true...")
    print("or b AND c are true... or both!")
```
## A common mistake
Remember that these operators work on booleans! A common mistake a lot of beginners make (even some more experienced programmers) is to forget this when using the or keyword.

Say we have a variable x, and we want to know if it's either 5 or 10. you might think to write this:
**common-mistake**
``` py
if x == 5 or 10
```
Because that makes sense to us as a sentence, but Python won't see it the same way! x == 5 is one expression, and 10 is another separate expression.

Because python implicitly casts numbers to booleans with an "is not zero" check, what we've actually written here is:
**common-mistake-2**
``` py
if (x == 5) or (10 != 0)
```

what we probably meant to write was this:
**mistake-fixed**
``` py
if x == 5 or x == 10
```
We've written two correct boolean expressions saying what we mean, there's no ambiguity here.

## Summary 
Like a lot of things in programming, at it's core boolean logic is very simple, but we can use it to do some pretty complicated things! Understanding the boolean operators we've just looked at will make it a lot easier for us going forward, and enable us to implement some pretty interesting logic into our code.