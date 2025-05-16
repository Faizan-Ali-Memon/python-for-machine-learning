class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        print("Your name and occupation is:", name, occupation)

    def intro(self):
        if self.occupation == 'actor':
            print("You are a good film actor")
        elif self.occupation == 'something':
            print("You are not an actor, you are something like a footballer")
        else:
            print("Occupation not recognized.")

# Create an object
human1 = Human("Faizan", "actor")

# Call the method
human1.intro()

# Access and print attributes
print(human1.name)
print(human1.occupation)
