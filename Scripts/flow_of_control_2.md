# Flow of control II: getin' loopy with it
Thinking of code as instructions: what if we want our instructions to repeat themselves? IE "do this until this", "repeat 5 times" and so on. Is there a way we can do this in Python.

Well, yes! yes there is, and that's what we'll be looking at in this session - they're called loops. As the name suggests, loops are flow-control statements that can direct block of code to be run, that is 'looped through' multiple times.

In python we have two types: for and while. We're going to explore both.

## While loops
Put very simply - a while loop is like an if statement, only where and if statement runs either once or not at all, a while loop can run as many times as you need it to, so long as it's condition remains true. 

[SIDE CAM]
Here's an example of a program that uses a while loop.
**example-while-loop**
```py
t = 10
print("Starship Python launching in...")

while t > 0:
    print(t)
    t = t - 1

print("Blast off!!!")
```
see how it's structured the exact same way as the ifs we looked at last time, that is: keyword, condition, body. It also work the same way, at least at first. If the condition is met, we enter into and execute the code in the body. The difference comes when we exit out of the body at the end of the block. 

Where an if statement will just continue on with the rest of the code, a while loop will actually go BACK and REVALUATE the condition. If it's still true, the block runs again, then again, then again and again until finally the condition evaluates to false, at which point we continue on with the program, never looking back.

Let's walk through this example. 't' starts with a value of 10 - the condition of the while loop is 't > 0'. t IS greater than 0, so this statement is true, and the condition is met. We enter into this block of code. 

See how the last line of the body re-assigns t to be one less than it's only value, so 9. Once we reach the end of the body, we check the condition again - t is now 9, 9 is still greater than 0, so true. We go again.

And we keep going, counting t down until we reach t = 0. 0 is not greater than 0, so this statement is now false, and the condition fails - and we properly exit out of the while loop. 

[CENTER CAM]
This raises an interesting question: can a while loop go on forever?

Indeed we can - while there are a few cases for loops that are, or at least COULD BE infinite, it's generally something we want to avoid, as it would cause our program to get stuck, never moving on from that loop. With the previous example we knew what we were doing: we knew we were starting at 10, we remembered to decrease it by 1 each time, so we knew eventually we'd reach zero and exit out of the loop. Depending on what we're trying to do, what condition we're trying to meet, and crucially what happens INSIDE the loop each time, we may not be so lucky. This is why we need to take care when using while loops - otherwise our program might get stuck.

*[Optional bit here but I appreciate I'm info dumping a bit]*
[SIDE CAM]
 But we can, if we're feeling mischievous, do it deliberately just to see what happens. Just for fun, here's an example of the infamous 'while true' loop.
 **infinite-while**
``` py
while True:
    print("You guys ever watch Groundhog's Day?")
```
So what actually happens if we press go on this thing. Well - it depends. Some IDEs and environments are clever, they'll see what's going on and call the program to a stop early - but this is actually surprisingly difficult so we can't count on it. 

[CENTER CAM]
Usually what happens is that it really does just keep going until something forces it to stop. This could be you - for instance by closing a window or pressing stop on your IDE. Most of the time this is fine, sometimes it can even be very useful for things like servers or background tasks, but depending what it's doing, how long it's been going, and how many resources that loop is taking up (and crucially whether or not that amount is growing) it can be a problem. In these cases quite often some other software, like the IDE or possibly your OS *[SIDE NOTE: OS - Operating System, the software that runs your whole computer]* may step in and gently suggest you let it stop the process, or just stop it without asking.

## For loops
For loops are a bit different, they're also our first example of a statement that needs two keywords:
**example-for.png**
``` py
for item in iterable:
    print(item)
```
For loops rely on some collection of items to work - in the context of a for loop we call this an iterable, that is something that can give us multiple elements to iterate through. The for loop will run once for each of those elements. Remember our collection data types like lists - these are great examples of iterables. let's see this in action.

[SIDE CAM]
**for-members-list**
``` py
members = ["Gary", "Alex", "Neil"]

for item in members:
    print("Hello, " + item + "!")
```
Here we have a list of names we're going to iterate through, which we've stored in a variable 'members'. We then open up a for loop - starting with the 'for' keyword, then a new variable name, then the 'in' keyword, then the name of our collection - or our iterable. 

This list has three elements, so the loop runs 3 times - simple enough. Where it gets interesting is the variable `item` *[underline/highlight uses of `item` in above]*. This is what we call the 'loop' or  'iteration variable' - a special variable that is defined automatically at the start of the for loop, and takes the value of each element in the iterator one at a time. 

For this example, see how 'item' takes on the value of every name in the list, starting from the 0th *[SIDE NOTE: Remember - list indexes start at 0!]*. *[show output of above code]*. We can also iterate through tuples, sets, and dictionaries much the same way!

[CENTER CAM]
The name of the loop variable doesn't actually matter too much. Some common names used by convention include "item", "element", and "i" - but so long as it's a valid variable name, and doesn't conflict with anything else, you can pick whatever. Just like any other variable, though, its advisable to pick a name that makes sense to you, and ideally will still make sense when you come back to it after not having looked it for a month...!

For the above example *[put back on screen if theres room]*, "member", "name" or even "person" would have all been perfectly sensible choices, but maybe not "x", or "thing", or "ftftderf".
**sensible-vs-not-sensible**

## Extra sugary bits
That's it, just two different kinds of loops - 'for' and 'while'. But before we wrap up, there are a couple of fun features of loops that python has built in. They're also examples of what we call "syntactic sugar" - that is features of a language that don't add anything new, and don't make anything possible that wouldn't have been possible without them, but make the actual code simpler to write and easier to read.

Computer Scientists often like food metaphors, so, we use the metaphor that it makes the code "sweeter" for the human writing and reading it.

[SIDE CAM]
The first is the 'continue' keyword
**continue**
``` py
my_list = [1, 2, 3, 4, 5]

for i in my_list():
    if i == 3:
        continue
    print(i)
```
Remember that loops, by nature, can run multiple times. We call each one of those runs an 'iteration'. So for this example here this loop will have 5 iterations, one for each element in 'my_list'

When a program encounters a 'continue' statement, it exits whatever iteration we're in early - and moves on to the next one. We can see here *[show code output]* that the number 3 doesn't get printed.

Next up is 'break'
**break**
``` py
my_list = [1, 2, 3, 4, 5]

for i in my_list():
    if i == 3:
        continue
    print(i)
```
If you like, you can think of break as a 'super continue'. That is, it not only skips whichever iteration it's currently in, but all subsequent ones as well - exiting (or 'breaking' out of) the whole loop. See here no number after 2 get printed.

[CENTER CAM]
Finally, a brief word on loop variables. Did you know that we can have for loops with multiple loop variables? They look like this:
**multiple-loop-variables**
``` py
for item1, item2 in some_iterable
```
Two variables, two different names, comma separated. This doesn't work all the time - most of the time it just wouldn't make sense. We're only interested in one element at a time after all. But, there are a few exceptions. The only one we're likely to need in this course it when iterating through dictionary items.

Remember we said dictionaries contain pairs of keys and values. By default, when we go through a dictionary with a for loop, we only get the keys. But using this `.items()` method, we can go through both at once. 

[SIDE CAM]
Here's what it looks like
**for-members-dictionary**
``` py
members = {
    "drums": "Neil",
    "bass": "Gary",
    "vocals": "Gary",
    "guitar": "Alex"
}

for key, value in members.items():
    print(value + " is on " + key)
```
We have a dictionary which maps the names of members of a band to the instrument they play. `members.items()` will iterate through every key-value pair in the dictionary, of which there are 4. We can see that each pair gets unpacked to two loop variables - which we've called key and value - which we can then reference separately in the body of the loop.

When we run it, we get this *[show code output]*.

[CENTER CAM]
There are other use cases for this feature, however dictionary key-value pair are by far the most common. Learning about how it works and where else we can use it can be super interesting if your curious, and want to know more *[maybe flash up some easily google-able terms like "packing and unpacking", "multiple loop variables" and even "itertools" for those curious...?]* though it's by no means essential.

## Summary
With this we've got the fundamentals of flow-of-control covered. We can go beyond thinking of our code as top-to-bottom step-by-step and start thinking of it as more dynamic and flexible. Already we have a toolkit to start tackling some simple - and potentially even some quite complicated - problems, and build solutions. Or at least, we will once we take time to strengthen what we've learned though exercises.

But that's not to say there's not more to cover! In the next sessions, we'll be exploring exactly how function work, and how we write our own.