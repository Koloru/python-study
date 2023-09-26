# 2D lists are lists inside of a list
# useful for grid like data or matrices of data

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["ginger", "pechay", "carrot", "tomato"]
meats = ["pork", "chicken", "fish", "shrimp"]

groceries = [fruits, vegetables, meats]

print(groceries)

fruits.append("Jerky")
groceries[0][1] = "tangerine"

# 2D list of lists
num_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


