weight = input("Enter weight in kg: ")

try:
  weight = float(weight)
except ValueError:
  print('You have entered an invalid weight, please try again')
  quit()

height = input("Enter height in m: ")

try:
  height = float(height)
except ValueError:
  print('You have entered an invalid height, please try again')
  quit()


bmi = weight / (height * height)

if bmi <18.5:
    print("You are underweight!")
elif bmi >= 18.5 and bmi <23:
    print("You are in normal weight!")
elif bmi >=23 and bmi <27.5:
    print("You are overweight!")
else:
    print("You are obese!")
