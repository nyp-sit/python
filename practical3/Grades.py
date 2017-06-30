score1 = int(input('Enter score for test 1 '))
test1 = int(input('Enter percentage for test 1 '))
score2 = int(input('Enter score for test 2 '))
test2 = int(input('Enter percentage for test 2 '))
score3 = int(input('Enter score for test 3 '))
test3 = int(input('Enter percentage for test 3 '))
exam = int(input('Enter your exam score '))
score = (score1 * test1 / 100) + (score2 * test2 / 100) + (score3 * test3 / 100) + exam/2
print('Your final score is ', score)
