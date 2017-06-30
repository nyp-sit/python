sum = 0
num = int(input("Enter number: "))

if num<2:
    print("Error")
else:
    i = 1
    while i <= num :
        if(i%2 == 0):
            sum = sum+i
        i += 1
print("Sum is", sum)
