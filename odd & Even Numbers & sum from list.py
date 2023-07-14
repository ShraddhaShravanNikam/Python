#odd & Even Numbers
a=[20,30,50,90,71,55]
i=0
sum_e=0
sum_o=0
while(i<len(a)):
    if(a[i]%2==0):
        print(i," Even value = ",a[i])
        sum_e=sum_e+a[i]
    else:
        print(i,"Odd value = ",a[i])
        sum_o=sum_o+a[i]
    i=i+1
print("Sum of Even Numbers =",sum_e)
print("Sum of Odd Numbers =",sum_o)
