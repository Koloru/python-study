

items = []
prices = []

item = ""

while True:
  item = input("Enter an item(q to quit): ")
  if item.lower() == "q":
    break
  else:
    price = float(input("Enter price: "))
    items.append(item)
    prices.append(price)


print(items)
print(prices)
