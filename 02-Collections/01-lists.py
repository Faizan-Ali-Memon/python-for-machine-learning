items = ["Fruit", "Pasta", "Chips", "Bread"]
print("Original list:", items)

# Update an item
items[2] = "Veggies"
print("Updated list:", items)

# Append item correctly
items.append("Butter")
print("After append:", items)

# Insert item at specific position
items.insert(1, "Sugar")
print("After insert:", items)

# Concatenate two lists
home = ["Fruits", "Pasta", "Veggies"]
other = ["Shampoo", "Soda"]
combined = home + other
print("Combined list:", combined)

# Length of list
print("Length of combined list:", len(combined))

# Membership test
print("Is 'Fruits' in combined list?", "Fruits" in combined)
