# Tuple (immutable list)
point = (5, 6)
print("Point coordinates:", point[0], point[1])

# Dictionary (key-value store)
d = {'joe': 3455332222, 'tom': 2142423223, 'samir': 892382}
print("Joe's number:", d['joe'])

# Add new entry
d["sam"] = 832938293
print("After adding Sam:", d)

# Delete entry
del d['sam']
print("After deleting Sam:", d)

# Iterate over dictionary keys and values
for key in d:
    print('Key:', key, 'Value:', d[key])

for k, v in d.items():
    print("Key:", k, "Value:", v)

# Check membership
print("Is 'tom' in dict?", 'tom' in d)
print("Is 'sam' in dict?", 'sam' in d)

# Clear dictionary
d.clear()
print("After clear:", d)
