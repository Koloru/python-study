# Lists are ordered collections in python
# Changeable
# Can have duplicates
# The same as arrays in other languages

names = ["John", "Tina", "Kent", "Oliver"]

# in operator is used to find a value in a collection
# Will check if john is in names
"John" in names

# Reassignment
names[0] = "Jean"

# Appending to the end of the list / Add element to the end of the list
names.append("Barbara")

# Remove an element in a list
names.remove("Tina")

# insert something at index and rearrange the indexes of the other elements
names.insert(0, "Clark")

# Sort in alphabetical order
names.sort()

# reverse a list
names.reverse()

# Remove all elements
# names.clear()

names.append("Kent")

print(names.count("Kent"))
# count how many an item is in the list


# Sets
# Sets are unordered and immutable
# No duplicates are allowed
# Add and remove an item
# You cannot reassign items

characters = {"Yoshi", "Mario", "Luigi", "Peach"}

# Add item to a set
characters.add("Boo")

# Remove item from a set
characters.remove("Yoshi")
# Remove whatever element is first

# but the first element will be random
characters.pop()

# remove all items
characters.clear()


for character in characters:
  print(character)


# Tuples
# Ordered and unchangeable
# faster than lists
# Duplicates are Okay

friends = ("Yoshi", "Mario", "Luigi", "Peach")

friends.index("Yoshi")