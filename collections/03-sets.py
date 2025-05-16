# Creating and printing a set
basket = {'orange', 'mango', 'grapes'}
print("Original basket:", basket)

# Adding an item
basket.add("Peach")
print("After adding Peach:", basket)

# Frozenset (immutable set)
a = frozenset([4, 5, 6])
try:
    a.add(7)  # Will raise AttributeError
except AttributeError:
    print("Cannot add item to frozenset")
finally:
    print("Frozen set:", a)
