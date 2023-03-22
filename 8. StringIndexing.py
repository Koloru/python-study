# Indexing lets you access the elements of a sequence using [] (indexing operator)
#  has 3 fields [start: end: step]


full_name = 'John_Doe'

# get only the first name "John" in full_name
# Start at the 0 place up to the 4th place

# John
full_name[0:4]
print(full_name[0:4])


# get only last name "Doe" in full_name
# not putting a value after the colon means it will go to the end of the sequence
full_name[5:]

# getting the last character
full_name[-1]


# print every 2 characters of the sequence
# if you put blank on the start and end python will assume you need the whole string
full_name[::2]

# reverse a string
full_name[::-1]
