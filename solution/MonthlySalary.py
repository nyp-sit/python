grossSalary = float(input("Gross Salary:"))
monthlySalary = grossSalary / 12
cpf = 0.2*monthlySalary
takeHome = monthlySalary - cpf - 1500
print("The monthly take-home pay is $", takeHome)
