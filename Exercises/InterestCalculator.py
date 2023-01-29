principle = 0 
rate = 0
time = 0

while principle <= 0:
  principle = float(input("Enter Principle Amount: "))
  if principle <= 0:
    print("Principle can't be less than zero or be zero")

while rate <= 0:
  rate = float(input("Enter Rate Amount: "))
  if rate <= 0:
    print("Rate can't be less than zero or be zero")

while time <= 0:
  time = float(input("Enter Time Amount: "))
  if time <= 0:
    print("Time can't be less than zero or be zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")