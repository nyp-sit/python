print('This program will store 10 numbers')

numList = []

for i in range(10):
    msg = 'Enter number #' + str(i+1)
    num = int(input(msg))
    numList.append(num)

print('The lowest number in the list:', min(numList))
print('The highest number in the list:', max(numList))
print('The total of the number in the list:', sum(numList))

print('The average of the number in the list:', sum(numList)/len(numList))
