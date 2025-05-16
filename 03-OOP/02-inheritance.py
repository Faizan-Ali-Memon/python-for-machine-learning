class Vehicle:
    def __init__(self):
        print("Hello, here is the main class Vehicle")

    def general_usage(self):
        print("I am used for transportation")

class Car(Vehicle):
    def __init__(self):
        print("Hello, here is the Car class")
        self.wheels = 4
        self.usage = "For family"

    def specific_usage(self):
        print("Car is used for family and the office")

    def __str__(self):
        return f"This is a Car with {self.wheels} wheels, used for {self.usage}"

class MotorCycle(Vehicle):
    def __init__(self):
        print("Here is the Motorcycle class")
        self.wheels = 2
        self.usage = "Racing"

    def specific_usage(self):
        print("Motorcycle is used for racing")

    def __str__(self):
        return f"This is a Motorcycle with {self.wheels} wheels, used for {self.usage}"

# Create Car object
c = Car()
c.general_usage()
c.specific_usage()
print(c)

# Create Motorcycle object
m = MotorCycle()
m.general_usage()
m.specific_usage()
print(m)
