

sum = 0
num = int(input("Enter number: "))

if num<2:  #part b
    print("Error")
else:
    for i in range(1, num+1):
       if(i%2 == 0):  #part b
            sum = sum+i

print("Sum is", sum)
