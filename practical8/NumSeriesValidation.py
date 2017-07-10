print('This program will store 20 numbers')

numList = []

count = 1

while count <=10:
    status = True
    msg = 'Enter number #' + str(count)
    try:
        num = int(input(msg))
    except ValueError:
        print('You have entered an invalid number, please re-enter again')
        status = False

    if status == True:
        numList.append(num)
        count +=1

print('The lowest number in the list:', min(numList))
print('The highest number in the list:', max(numList))
print('The total of the number in the list:', sum(numList))

print('The average of the number in the list:', sum(numList)/len(numList))
