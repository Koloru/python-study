plm = int(input("Enter Prelim Grade: "))
mdt = int(input("Enter Midterm Grade: "))
fnl = int(input("Enter Final Grade: "))

total = int((plm + mdt + fnl)/3)

print("Grade is:", total)


match total:
  case total >= 95:
    # print("The equivalent letter grade of", total, "is A.")
# elif total >= 90:
#     print("The equivalent letter grade of", total, "is B.")
# elif total >= 83:
#     print("The equivalent letter grade of", total, "is C.")
# elif total >= 74:
#     print("The equivalent letter grade of", total, "is D.")
# else:
#     print("The equivalent letter grade of", total, "is F")