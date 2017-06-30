gpa = 0
total_grade_point = 0
total_credit = 0
for i in range(1, 6) :
    credit = int(input('Enter the credit for Module ' + str(i) + ": "))
    gpa = float(input('Enter your GPA for Module ' + str(i) + ": "))
    total_grade_point += gpa * credit
    total_credit += credit
print('Your cumulative GPA for 5 modules are', total_grade_point/total_credit)
