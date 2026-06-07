print("Welcome to the Tip calculator: \n")

Bill=input("What is total bills in dollars?:")
Tip=input("How much percentage of Bill youwant to tip: ie: 10, 20 or 30  :")
Bill=float(Bill)
Tip=int(Tip)
Bill=(round(Bill,2))
Tip=int(Tip)

print(f"your total bill is {Bill} and you tiped {Tip}% ")

Tipvalue=round((Tip/100 *Bill),2)

totalBill=Bill+Tipvalue

print(f"your total bill is {totalBill}")

print("\n")
person=int(input("Enter number of friends to split bills  :"))

Each=round(totalBill/person,2)

print(f"Each person will pay {Each}$ amount \n")



