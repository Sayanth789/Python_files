class Engine:
    def __init__(self, hourse_power):
        self.hourse_power = hourse_power

class Wheel:
    def __init__(self, size):
        self.size = size 

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make 
        self.model = model 
        self.horse_power = horse_power
        self.wheels  = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.horse_power} (hp) {self.wheels[0].size} in"

car = Car("Ford Mustang", model="mustang", horse_power=500, wheel_size=18)


print(car.display_car())
                        

