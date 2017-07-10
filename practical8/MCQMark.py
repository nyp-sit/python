answerList = ['C', 'D', 'B', 'A', 'B', 'D', 'A', 'C', 'D', 'C']

mark = 0

while True:
    studentAttempt = []
    print('Please enter your Review Exercise answer')
    for n in range(10):
        studentAttempt.append(input('MCQ #%d: ' %(n+1)))

    count = 0
    for i in range(10):
        if answerList[i] == studentAttempt[i]:
            count += 1

    if count > mark:
       mark = count

    print('You have %d correct answer and %d wrong answer' %(count, 10-count))

    tryAgain = input("Do you want to try again? (Y/N)")

    if tryAgain=='Y' or tryAgain =='y':
        continue
    else:
        break

print('Your mark for Review Exercise is %.1f' %(mark/2))
print('Review Exercise Answers: ')
print(answerList)
