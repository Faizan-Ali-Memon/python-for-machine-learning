number = [3, 4, 5, 6, 7]

# List comprehension to get even numbers
even = [i for i in number if i % 2 == 0]
print("Even numbers:", even)

# Set from list (removes duplicates)
numbers = set([3, 4, 5, 32, 3, 4, 5])
print("Set of numbers:", numbers)

# Creating dictionary from two lists
cities = ['Lahore', 'Isb', 'Khi']
countries = ['Pakistan', 'India', 'UK']

zipped = zip(cities, countries)
d = {city: country for city, country in zipped}
print("City-country dictionary:", d)
