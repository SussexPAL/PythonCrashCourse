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


class PalCar(Car):
    def __init__(self, num_plate: str):
        # super().__init__(num_plate, colour, seats)
        super().__init__(num_plate, "purple")
    
    def horn(self):
        print("BEEEEP!!")


class FlyingCar(Car):
    def __init__(self, num_plate: str, colour: str):
        super().__init__(num_plate, colour)
        self.wheels = 0


class SelfDrivingCar(Car):
    def __init__(self, num_plate: str, colour: str):
        super().__init__(num_plate, colour)
        self.steering_wheel = False


class FutureCar(FlyingCar, SelfDrivingCar):
    pass


class SuperPalCar(PalCar):
    def add_fuel(self, liters):
        print("No need to add fuel! The SuperPalCar runs on solar-power and wishes!")
    
    def drive(self, km):
        self.km_driven += km
        print("{} km drive, no fuel used!".format(km))