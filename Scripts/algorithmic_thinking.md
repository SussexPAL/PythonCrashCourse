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

To start this course, we'll spend some time focusing on the algorithm part, before we look at building programs (which will be the majority of the course). The reason algorithms are so important is that they're so much more context and platform independent, and flexible in the way they're written, than a program.

When working with a programming language, that language will have it's own rules as to exactly how things need to be written (called its syntax). Who ever is writing the program needs to understand and follow these rules, otherwise the program simply cannot be run.
*[some deliberately slightly scary looking code here + DELIBERATE MISTAKE]*
`thing: ThingType = get_thing()`
`do_this(thing)`
`thing.do_that(`
`return`
Remember: while computers are extremely smart, they can also be extremely stupid and stubborn, and refuse to work because you left out a closing bracket.
*[circle incorrect brackets, and show program error, or crashing... I like the idea of a PAL themed BSoD personally...!]* 

Algorithms, on the other hand, are a lot more forgiving. You algorithm still needs to make sense, and needs to be 'correct' for whatever it's trying to do. But beyond that, so long as its reasonably understandable, you can kind of write it however you want:
* as a flowchart:
*[START -> GET THING -> DO THIS -> DO THAT -> STOP]*
* step by step instructions
    1) get the thing
    2) do this
    3) do that
* or just written down...
*["First, get the thing. Then do this. Finally, do that"]*
... in whatever language you want
*["まず、 アレを手に入れる。 それからこれをする。 最後にあれをする。"]*

# Writing an algorithm
We're now going to practice that this problem-to-algorithm-to-solution process using a very simple, every day example. At least, every day for me, because I love tea *[I do actually have a purple sussex travel mug if we want a shot for this bit... just sayin']*. The problem is: wanting a cup of tea. Our solution: make one. For this example - this problem space - we'll say we have a kettle, a box of teabags, a mug etc. but for some reason we (or whoever it is who's going to be making our tea) doesn't know what to do with them.

What we would do is write out the step by step instructions for making tea such that they can be followed by anyone. We're going to write this as though it were for a fake program, this style is called *'pseudocode'*, it gives us the structure and definition of code, without the risk that something could go wrong if we make a minor grammatical mistake.

`kettle.fill (enough water for mug)`
`kettle.start`
`GET teabag FROM box`
`PUT mug teabag`

`WAIT UNTIL kettle.done`
`mug fill kettle.water`

`WAIT UNTIL minutes 2`
`mug take_out teabag`

*[might be worth holding on this for a bit, so people can give it a proper read, or at least doing the next few lines a bit more slowly]*

Maybe this looks a little strange, and that okay. Remember, this is fake code - not for a real programming language, and as such the exact wording is not important so long as it's interpretable. You can that this looks somewhat resembles computer code, or if you've never seen computer code you can just think of it as very literal and blunt instructions.

The great thing about algorithms as that they can be completely scalable for as much or as little detail as you need them to be. Here we've made the assumption that whoever or whatever can interpret the individual instructions...

*[focus on]* `kettle fill (enough water for mug)`
... but if we needed to, or wanted to, we can break those instructions down even further.
`* take kettle off stand`
`* take kettle to tap`
`* turn on tap`
`* ... etc`

Or on the other hand if 'making tea' was just one step of a much larger algorithm, and we could assume the end user already knew how to make tea, we could condense it down to just one line.
`GET apple FROM fridge`
`GET bread FROM cupboard`
`PUT bread toaster`
`toaster.start`
`make_tea`
`WAIT UNTIL toaster.done`
It depends entirely on what already HAVE, what we assume we KNOW, and what we NEED. That is what we mean by the problem space. 

# Bubble sort
Making tea is a good example to start with when it comes to writing step-by-step algorithms. But it's unlikely to be the kind of problem we'll be writing code for any time soon. Lets look a similarly simple, but more abstract (more computer-y) example. The kind we very much would be writing code for: sorting a list of numbers.

*[1, 17, 3, 16, 7, 14, 2, 20, 10, 18]*

The problem space here: 
* we have a list of numbers
* we can move numbers around in the list *[maybe show a number being moved]*
* we can compare numbers by size *[1 is less than 17, 17 is greater than 3 etc.]*
* we can't add, change, or remove and numbers from the list
* we want the list to be in order, smallest to largest

We're going to take a look a famous solution to this problem: the bubble sort algorithm.
