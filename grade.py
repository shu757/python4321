# Python Program - Calculate Grade of Student

a,b,c,d,e=eval(input("Enter marks obtained in 5 subjects: "))
mark1 = input();

sum = (a+b+c+d+e)
average = sum/5
print(average)
if(average>=91 and average<=100):
    print("Your Grade is O");
elif(average>=81 and average<=90):
    print("Your Grade is A");
elif(average>=71 and average<=80):
    print("Your Grade is B");
elif(average>=61 and average<=70):
    print("Your Grade is C");
elif(average>=51 and average<=60):
    print("Your Grade is D");
elif(average>=41 and average<=50):
    print("Your Grade is E");
elif(average>=0 and average<=40):
    print("Your Grade is F");
else:
    print("Strange Grade..!!");
