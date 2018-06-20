#program to convert time in sec to hh:mm:ss
seconds=int(input("enter the no of seconds"))
#calculate the hours,minutes and seconds
hours=seconds/3600
seconds=seconds%3600

minutes=seconds/60
seconds=seconds%60

print("the time is: ","%02d:%02d:%02d"%(hours,minutes,seconds))
