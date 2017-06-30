weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

bmi = weight / (height * height)

if bmi <18.5:
    print("You are underweight!")
elif bmi >= 18.5 and bmi <23:
    print("You are in normal weight!")
elif bmi >=23 and bmi <27.5:
    print("You are overweight!")
else:
    print("You are obese!")
