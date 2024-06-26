# Video - Algorithmic thinking

*[for now I'm leaving out the "hello, welcome, we're pal etc" stuff I want the wording from @dexter]*

## What is an algorithm - and why are they so important?
The aim of this course is to get us comfortable with writing code, designing programs to solve problems, and even using some simple machine learning. But we're not actually going to jump straight into the programming straight away (although we will be soon). Before we do that it's worth taking a little time to illustrate the kind of logic we want to use in order go from some problem space, to some potential solution, to a working implementation of that solution.

*[Some diagram: PROBLEM  -> SOLUTION -> IMPLEMENTATION]*

For this, we want to practice *algorithmic thinking*. That is, breaking down the solution to a problem into an objective set of instructions. Instructions that could, in theory, be followed by anyone, anywhere; a bit like a cooking recipe...
*[PROBLEM: I want to make a cake -> SOLUTION: a cake recipe -> IMPLEMENTATION: me making a cake]*
...or a assembly instructions for a piece of furniture. 
*[PROBLEM: Un-assembled furniture  -> SOLUTION: assembly instructions -> IMPLEMENTATION: assemble furniture according to instructions]*
In computer studies, we call this kind of sequential finite and definite set of instructions and *algorithm* with which we can write a solution in the form of a program.
*[Diagram changes: PROBLEM  -> POTENTIAL SOLUTION -> ALGORITHM -> PROGRAM]*

To start this course, we'll spend some time focusing on the algorithm part, before we look at writing programs (which will be the majority of the course). The reason algorithms are so important is that they are context and platform independent and flexible in the way they're written, so long as that they are interpretable and correct.

Compare this to programming. When working with a programming language, that language will have it's own rules as to exactly how things need to be written (called its syntax). Who ever is writing the program needs to understand and follow these rules, otherwise the program simply cannot be run.
*[some deliberately slightly scary looking code here + DELIBERATE MISTAKE]*
`thing: ThingType = get_thing()`
`do_this(thing)`
`thing.do_that(`
`return`
Remember: while computers are extremely smart, they can also be extremely stupid and stubborn, and refuse to work because you left out a closing bracket.
*[circle incorrect brackets, and show program error, or crashing... I like the idea of a PAL themed BSoD personally...!]* 

Algorithms, on the other hand, are a lot more forgiving. You algorithm still needs to make sense, and still needs to accomplish whatever it's trying to do. But beyond that, you can kind of write it however you want:
* as a flowchart:
*[START -> GET THING -> DO THIS -> DO THAT -> STOP]*
* step by step instructions
    1) get the thing
    2) do this
    3) do that
* or just written down in plain english...
*["First, get the thing. Then do this. Finally, do that"]*
... or any other language you want language you want
*["まず、 アレを手に入れる。 それからこれをする。 最後にあれをする。"]*

# Writing an algorithm
We're now going to practice that this problem-to-algorithm-to-solution process using a very simple, every day example. At least, every day for me, because I love tea *[I do actually have a purple sussex travel mug if we want a shot for this bit... just sayin']*. The problem is: wanting a cup of tea. Our solution: make one. For this example - this problem space - we'll say we have a kettle, a box of teabags, a mug etc. but for some reason we (or whoever it is who's going to be making our tea) doesn't know what to do with them.

What we would do is write out the step by step instructions for making tea such that they can be followed by anyone. We're going to write this as though it were a fake program, this style is called *'pseudocode'*, it gives us the structure and definition - and overall feel - of code, without the risk that something could go wrong if we make a minor grammatical mistake.

kettle.fill (enough water for mug)
kettle.start
GET teabag FROM box
PUT mug teabag

WAIT UNTIL kettle.done
mug fill kettle.water

WAIT UNTIL minutes 2
mug take_out teabag

*[might be worth holding on this for a bit, so people can give it a proper read, or at least doing the next few lines a bit more slowly]*

Maybe this looks a little strange, and that okay. Remember, this is basically pretend code - not for a real programming language, and as such the exact wording is not important so long as it's interpretable. You can see that this looks somewhat resembles computer code, or if you've never seen computer code you can just think of it as very literal and blunt instructions.

Algorithms are completely scalable for as much or as little detail as you need them to be depending on the context of the problem. Here we've made the assumption that whoever or whatever can interpret the individual instructions like "kettle.fill" or "PUT mug teabag"

... but if we needed to, or wanted to, we can break those instructions down even further.
* take kettle off stand
* take kettle to tap
* turn on tap
* ... etc

Or on the other hand if 'making tea' was just one step of a much larger algorithm (say making breakfast), and we knew whoever we were writing for knew how to make tea, we could condense it down to just one line.
GET apple FROM fridge
GET bread FROM cupboard
PUT bread toaster
toaster.start
make_tea
WAIT UNTIL toaster.done
It depends entirely on what already HAVE, what we assume we KNOW, and what we NEED. That is what we mean by the problem space. 

# Bubble sort
Making tea is a good example to start with when it comes to writing step-by-step algorithms. But it's unlikely to be the kind of problem we'll be writing code for any time soon. Lets look a similarly simple, but more abstract (more computer-y) example. The kind we very much would be writing code for: sorting a list of numbers.

*[1, 17, 3, 16, 7, 14, 2, 20, 10, 18]*

Lets break down the problem space here: 
* we have a list of numbers
* we can move numbers around in the list *[maybe show a number being moved]*
* we can compare numbers by size *[1 is less than 17, 17 is greater than 3 etc.]*
* we can't add, change, or remove and numbers from the list
* we want the list to be in order, smallest to largest

We're going to take a look a famous solution to this problem: the bubble sort algorithm. We'll be talking through this algorithm in simple English (which remember is all we really need), then taking a brief look at some other, perhaps more formal, ways of it being written out.

*[Okay I'm trusting you to come up with the suitable graphics so I'll leave sufficient space between steps]*

Bubble sort starts like this: compare the first and second elements (that is, numbers) in the list. 1 and 17. Are they in the right order? In this case they are, so we move on.

Next, we compare the second and third elements in the list, so 17 and 3. Again we ask, are they in the right order? In a sorted list, we'd expect 3 to come before 17, so they cannot be in the correct order here. What we do is reverse the order of just these two numbers, before moving on.

*[1, 3, 17, 16...]*

Next we compare the third and fourth elements of the list as it is NOW (remember, we just swapped the last two numbers) so here we're comparing 17 and 16. Again, we'd expect 16 to come before 17, so we swap them around...

... and we move on to the 4th and 5th, then the 5th and 6th, then the 6th and 7th and so on until we reach the end of the list, with the 2nd to last and last elements.

Although, even after one pass this list isn't fully sorted. So, we go again, starting again from the 1st and 2nd elements. And we keep repeating until we manage to complete one full pass of the list without changing any numbers.

We'll know we're done then, as if no numbers in the list come before any numbers that are smaller than themselves, then the list must* be sorted.

This algorithm can be applied to any list of any length, with any numbers in it. It will always work: whether we only needed to swap two number around, whether it would take hundreds of cycles to order it correctly, or even if it was in the right order to begin with, we will ALWAYS end up with a perfectly sorted list.

And that's it, that's bubble sort. So called because the numbers rise or 'bubble up' through the list into the correct position over time. We can represent this same algorithm in several different ways:
* pseudocode
* flowchart
* step-by-step

And also worth noting is that this is far from the only way to order a list, that is there are multiple correct algorithms for this problem space. In fact bubble sort is actually one of the slowest ways of doing it! but it does have a certain simplicity and elegance to it, which makes it a favorite example in education.

## summery

So that's it, we know what an algorithm is. Ideally, we should always have some idea of what algorithm, that is what step by step solution, we want to implement after looking at a problem, but before we even write our first line of code. With this in mind, you're ready to learn to code.