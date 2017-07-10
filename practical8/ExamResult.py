examResult = {'Jane': [75, 80, 85], 'John':[60, 68, 74], 'Jerome':[81, 63, 77], 'Jason':[55, 76, 67], 'Jessica':[62, 45, 68], 'Joanne':[52, 47, 51]}

name = input('Enter student name:')
studentResult = examResult.get(name, 'Student does not exist!')

print("Results of", name)
print("=================================")
print('English:', studentResult[0])
print('Math:', studentResult[1])
print('Science:', studentResult[2])

englishMark = 0
mathMark = 0
scienceMark = 0

print('======================================')
for key in examResult:
    average = (examResult[key][0] + examResult[key][1] + examResult[key][2])/3
    print('Average marks of', key, ":%.2f" %average)

    englishMark +=examResult[key][0]
    mathMark += examResult[key][1]
    scienceMark += examResult[key][2]

englishMark = englishMark/len(examResult)
mathMark = mathMark/len(examResult)
scienceMark = scienceMark/len(examResult)
print('===============================================')
print('Average results for English:%.2f' %englishMark)
print('Average results for Math:%.2f' %mathMark)
print('Average results for Science:%.2f' %scienceMark)

