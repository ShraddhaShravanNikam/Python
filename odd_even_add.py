#Sum of odd and even numbers
i=1
sum_e=0
sum_o=0
while(i<=10):
    if(i%2==0):
        print("Even =",i)
        sum_e=sum_e+i
    elif(i%2==1):
        print("Odd =",i)
        sum_o=sum_o+i
    i=i+1
print("Sum of even =",sum_e)
print("Sum of odd =",sum_o)



