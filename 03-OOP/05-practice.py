# OOP Practice Script

# --- Practice 1: Create a Class and Use Methods ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Faizan", 22)
p1.greet()

# --- Practice 2: Inheritance ---
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Kitty")
dog.speak()
cat.speak()

# --- Practice 3: Multiple Inheritance ---
class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()

# --- Practice 4: Decorator to Measure Execution Time ---
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)*1000:.2f} ms")
        return result
    return wrapper

@time_it
def count_to_n(n):
    total = 0
    for i in range(n):
        total += i
    return total

print("Sum:", count_to_n(1000000))
