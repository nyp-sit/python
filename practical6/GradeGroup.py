
total_grade_point = 0
total_credit = 0
num = 0
while True :
    code = input('Enter the module code (type end to finish) : ')
    if code == 'end' :
        print('Your cumulative GPA for %d modules are %.2f' % (num, total_grade_point/total_credit))
        break
    elif code != 'IT1111' and code != 'IT1213' and code != 'IT1101' and code != 'ITP111' and code != 'IT1110' :
        print('You have entered an invalid module code')
        continue
    credit = int(input('Enter the credit for module ' + code + " : "))
    grade = input('Enter your grade for ' + code + " : ")

    if grade == 'A' :
        gpa = 4.0
    elif grade == 'B+' :
        gpa = 3.5
    elif grade == 'B' :
        gpa = 3.0
    elif grade == 'C+' :
        gpa = 2.5
    elif grade == 'C' :
        gpa = 2.0
    elif grade == 'D+' :
        gpa = 1.5
    elif grade == 'D' :
        gpa = 1.0
    elif grade == 'F':
        gpa = 0
    else :
        print('You have entered an invalid grade!')
        continue
    print('Your GPA is %.1f for module %s that has %d credit point.  You earned %.1f grade points' % (gpa, code, credit, gpa * credit))
    num += 1
    total_grade_point += gpa * credit
    total_credit += credit

