# Object Oriented Programming part 4 - inheritance
Think about what the word 'inheritance' means in English - something which is passed down from one generation to another in a sort of parent-to-child or original-to-new way. This could be a name, or a language, or any kind of property like eye or hair colour.

This doesn't just apply to people but to objects as well, we might say a new model of car has "inherited" certain design features from the cars that came before it: like having four wheels, a fuel tank, and a steering wheel. These are all things we think of as fundamental to what a car is.

In OO design, inheritance means much the same thing. One class can inherit certain attributes from another. Let's take a look

## Inheritance in Python
Let's write a class for a car. We'll have some properties which are set in the constructor, and some which are set as defaults. We'll also include a couple of methods
``` py
class Car:
    def __init__(self, num_plate: str, colour: str):
        # Constructor params
        self.num_plate = num_plate
        self.colour = colour
        self.wheels = 4
        self.steering_wheel = True
        
        # More properties
        self.fuel = 0
        self.km_driven = 0
        
    def add_fuel(self, liters):
        # A method to add fuel
        self.fuel += liters
    
    def drive(self, km):
        # A method to drive the car, consuming fuel
        # won't work if there's not enough fuel
        fuel_needed = km / 8
        
        if fuel_needed > self.fuel:
            print("not enough fuel!")
            return
            
        self.km_driven += km
        self.fuel -= fuel_needed
        print("drove {} km and consumed {} liters of fuel".format(km, fuel_needed))
```

Now let's say we want to write another class for a specific model of car. Instead of copying out the whole definition again, let's use inheritance!
``` py
class PalCar(Car):
```
This is the Syntax python uses for inheritance. Starting with the opening line of the class definition, with these brackets that we haven't seen before. It is in these brackets we put the class we want to inherit from.

The syntax is very similar to writing parameters in a function, but don't get confused - they mean different things: one is for function definitions, the other is for class inheritance.

inheritance means that everything 'Car' does, 'PalCar' will also do. If we were to just leave it here with no further definition...
``` py
class PalCar(Car):
    # In Python, we can't *literally* leave expression bodies blank
    # so we use the 'pass' keyword instead.
    pass
```
It would be completely identical to car. We call this a 'subclass', which makes Car the 'superclass' *[SIDE NOTE: other terms include "parent and child class" and "base and derived" class]*. If we changed the superclass, the subclass would change, too.

From here we can add new attributes to PalCar, like methods and properties. Let's add a method for beeping the car horn!
``` py
class PalCar(Car):
    def horn(self):
        print("BEEEEP!!")
```
Now let's see how these classes work - we'll create two objects, one of the super 'Car' class, the other of the sub 'PalCar' class.
``` py
super_car_obj = Car("ABC 123", "white")
sub_car_obj = PalCar("XYZ 765", "purple")
```
We'll see that we can access any method or property of Car from the subclass PalCar, but if we try and access anything specific to PalCar from the Car superclass, we get an error!
``` py
sub_car_obj.drive(10)
sub_car_obj.add_fuel(5)
sub_car_obj.drive(10)
sub_car_obj.horn()
super_car_obj.horn() # The problem line

'''
not enough fuel!
drove 10 km and consumed 1.25 liters of fuel
BEEEEP!!
Traceback (most recent call last):
  File "c:\Users\PAL\learn_python\scope.py", line 5, in <module>
    super_car_obj.horn()
    ^^^^^^^^^^^^^^^^^^
AttributeError: 'Car' object has no attribute 'horn'
'''
```

## Overriding and Super calls
So far so good: we can inherit from a class, and add new properties to the subclass. But what if we also want to override properties of the superclass?

Let's say we want every PalCar object to be purple. Remember that 'Car' takes colour as one of the constructor arguments, but we don't want this to be an option for PAL cars. To do this, we would need to override the constructor.
``` py
class PalCar(Car):
    def __init__(self, num_plate: str):
        # Constructor params
        self.num_plate = num_plate
        self.colour = "purple"
        self.wheels = 4
        self.steering_wheel = True
        
        # More properties
        self.fuel = 0
        self.km_driven = 0
```
Overriding is essentially redefining, or replacing an original definition with a new one. Here we've written a new constructor for PalCar which will override Car's constructor which it inherits. See that now, colour is no longer accepted as an argument, it's always set to purple by default!

When you override an attribute, it will be overridden for that subclass only - the superclass will be unchanged.

In Python, you don't need any special syntax for this, it's written just the same as any other method definition. But you do need to make sure you've gotten the name right - if the name doesn't match the original method or property of the superclass, you won't have overridden anything, you'll have just defined something new and the original will still be there.

Re-writing a an overridden method is good if you want to completely change how it works, but here it seems kind of unnecessary: we're just changing one thing after all. Remember what we've said before about wanting to reduce redundancy in our code: "say something once, why say it again". Luckily there is a solution.

In python, we can use a special method called `super()`. Super allows a subclass to access any attributes of it's superclass. We do this by calling whichever method or property we want from a super call, like this:
*[Maybe highlight the line where super() is used, so it stands out a bit more]*
``` py
class Thing:
    def say_hello(self):
        print("Hello, from the Thing class!")


class OtherThing(Thing):
    def say_hello(self):
        print("OtherThing class, getting ready to say hello.")
        super().say_hello()


obj = OtherThing()
obj.say_hello()

'''
OtherThing class, getting ready to say hello.
Hello, from the Thing class!
'''
```

This helps us with our car example: instead of rewriting the whole thing, let's just call the super constructor, but this time passing 'purple' as one of the arguments:
``` py
class PalCar(Car):
    def __init__(self, num_plate: str): # No colour argument here...!
        super().__init__(num_plate, "purple") # It's passed to the super constructor as "purple"
```
The super constructor will run as normal, just like we already wrote it. Notice that this time we did explicitly call the `__init__` by name - normally it's done automatically. Calls from super are one of the few times you will need to do this for 'magic methods' like init. *[REMINDER: magic or 'dunder' methods are special methods with double underscores on either side. They have special syntax for calling them.]*

One class can have multiple subclasses - and those subclasses can have subclasses of their own! This can grow into large 'family trees' of classes - with their own uses and levels of complexity - all inheriting from one common superclass.

We could define flying cars with no wheels, self driving cars, even a "Super PalCar" subclass which you never need to refuel (somehow).
``` py
class FlyingCar(Car):
    def __init__(self, num_plate: str, colour: str):
        super().__init__(num_plate, colour)
        self.wheels = 0


class SelfDrivingCar(Car):
    def __init__(self, num_plate: str, colour: str):
        super().__init__(num_plate, colour)
        self.steering_wheel = False


class SuperPalCar(PalCar):
    def add_fuel(self, liters): # Overriding
        print("No need to add fuel! The SuperPalCar runs on solar-power and wishes!")
    
    def drive(self, km): # Overriding
        self.km_driven += km
        print("{} km drive, no fuel used!".format(km))
```

## A brief word on multiple inheritance
Can one class have multiple superclasses? That is, can we have a class inherit features from two different classes? The short answer is: yes!

Python does allow for multiple inheritance...
``` py
class FutureCar(FlyingCar, SelfDrivingCar):
    pass
```
... although not every language does. This is because it does introduce some problems: what if the two parent classes have conflicting properties? Or two methods with the same name that do different things, how would the child class know which one to inherit?

Python gets around this by having something called 'method resolution order'. If there is a conflict, one class takes priority, as determined by the order in which the superclasses where listed.

``` py
class A:
    def foo(self):
        print("A")

class B:
    def foo(self):
        print("B")

class AB(A, B):
    pass

class BA(B, A):
    pass

obj1 = AB()
obj2 = BA()

obj1.foo()
obj2.foo()

''' OUTPUT
A
B
'''
```

Multiple inheritance isn't very common, likely because Python is one of the few languages which supports it, and also because it can get pretty messy. wou won't need to use it in many cases, but it does have a few super interesting niche uses, which could be worth having a play around with once you've gotten comfortable with the fundamentals.

## Summary
Class inheritance is a very useful tool for big programming projects. It gets used everywhere from video games, to web apps, to machine learning. You'll see a lot not just in your own code, but in the design and documentation for programs you'll be using for yourself. So, Understanding how it works will be extremely useful in your ongoing coding journey.

