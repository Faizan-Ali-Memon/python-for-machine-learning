class Father:
    def skills(self):
        print("Programmer")

class Mother:
    def skills(self):
        print("Cooking Expert")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")

c = Child()
c.skills()
