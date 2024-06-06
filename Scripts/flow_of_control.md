So; we've started exploring some basic programming.

But; right now we're kind of using Python like a simple calculator. There's nothing wrong with this, but, we could go further and have a program that has the output vary a lot more.

When we covered variables and data types, you might remember that we covered something called a "boolean". A boolean is a value that can be either True, or False; or, 0 and 1.

We can combine this with something called an "if" statement - you can think of "if" as being asking the computer "When executing this code, only run it **if** this *condition* is true". The condition is a statement that will result in either True, or False.

We have a few "operators" for checking conditions. The first and simplest is two equals signs - this allows us to check if two values are the same.

For example, `2 == 2`, but, also, `2 == 3 - 1`. This seems fine, but, we can also use variables in place here. Let's say we have a variable named "foo", and, we put the word "hello" into it. In our program, we can write `if foo == "hello"`, and, some code will execute. If we change the value of "foo", the program will do something else instead.

There are other equality statements too. We can use the angle brackets as greater than and less than - it's always nice to remember the sign as being a mouth that's trying to eat the bigger one. For example `4 > 2` and `10 * 3 < 29 + 5`

We can also use exclamation equals as shorthand for "Not equals". For example, `"hello" != "world"`, `3 != 1`, and, `foo != "other_word"` (assuming `foo` is still `"hello"`).

All these operators will resolve down to either True or False - for example, if you write `print("hello" == "hi!")`, you will just see `False`! We can then use other keywords to chain multiple conditions together - for example, `not` will invert the output (e.g. `not "hello" == "hi!"` is `True`).

`or` will be true if one or more conditions are true - e.g. `"4 > 2 or 5 > 10`. Five isn't greater than 10, but, because 4 is greater than 2, the entire statement is true.

Finally, `and` requires *all* conditions in a statement to be true. Taking the same example, `4 > 2 and 5 > 10` - we will get `False` because five still isn't greater than 10. This is regardless of the fact 4 is bigger than 2 - becuase not *all* of the conditions are satisfied, the entire thing will return `False`.

- For loops

- Refresher on Range keyword (brought up in George's worksheet, but, let's properly explain it)

- While loops