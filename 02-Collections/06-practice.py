# Collections Practice

# --- Lists ---
print("1. Lists Practice")
fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)

# Add a new fruit and remove one
fruits.append("elderberry")
fruits.remove("banana")
print("Updated list:", fruits)

# Slice first 3 fruits
print("First three fruits:", fruits[:3])

# --- Tuples ---
print("\n2. Tuples Practice")
point = (10, 20)
print("Tuple point:", point)
try:
    # Tuples are immutable, this will raise an error
    point[0] = 15
except TypeError:
    print("Cannot modify a tuple!")

# --- Dictionaries ---
print("\n3. Dictionaries Practice")
phonebook = {'Alice': '1234', 'Bob': '5678', 'Charlie': '91011'}
print("Phonebook:", phonebook)

# Add a new entry
phonebook['David'] = '121314'
print("After adding David:", phonebook)

# Print all keys and values
for name, number in phonebook.items():
    print(f"{name}: {number}")

# --- Sets ---
print("\n4. Sets Practice")
colors = {'red', 'green', 'blue'}
print("Original colors set:", colors)
colors.add('yellow')
print("After adding yellow:", colors)

# Check membership
print("Is 'green' in colors?", 'green' in colors)

# --- List Comprehension ---
print("\n5. List Comprehension Practice")
numbers = list(range(1, 11))
squares = [n**2 for n in numbers if n % 2 == 0]
print("Squares of even numbers 1-10:", squares)

# --- Iterator with Custom Class ---
print("\n6. Iterator Practice")

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for i in MyRange(5, 10):
    print(i, end=" ")
print()

# --- Generator Practice ---
print("\n7. Generator Practice")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x, end=" ")
print()
