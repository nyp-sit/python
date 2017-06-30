#Convert seconds to hours, minutes and seconds
totalSec = int(input("enter seconds:"))
hour = totalSec//3600
minute = (totalSec //60)%60
second = totalSec % 60
print("%d seconds is %d hours, %d minutes and %d seconds" %(totalSec, hour, minute, second) )
