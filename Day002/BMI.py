weight=input("Enter your wight (kg) :\n")
height=input("enter your height in cm :\n")

weight=int(weight)
height=int(height)

heightSquare=(height**2)
BMI= weight/heightSquare
#implementing f string
print(f"your weight is: {weight} and your height is {height}")
Bmi=round(BMI,3)


print("The BMI is:",Bmi)


