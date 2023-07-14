#Arithmetic Function
'''def add(a,b):
    return a+b
print(add(30,20))
def sub(a,b):
    return a-b
print(sub(30,20))
def mul(a,b):
    return a*b
print(mul(30,20))
def div(a,b):
    return a/b
print(div(30,20))'''
#marks
'''m=[90,80,70,89,90]
def marks (m):
    sum=0
    i=0
    for i in m:
        sum=sum+i
    print(m)
    print("Sum =",sum)
marks(m)'''
#string Palllindrome
#x="I repaper my mobiles rotator"
'''def Pallindrome(x):
    y=x.split()
    print(y)
    i=0
    for i in y:
        #print(i)
        b=i[ : :-1]
        if(i==b and len(i)>1):
            print(i)
x="I repaper my mobiles rotator"
Pallindrome(x)'''

#Super Prime
'''def prime(no):
    i=2
    flag=0
    rem=0
    sum=0
    while(i<no):
        if(no%i==0):
            flag=1
            break
        i=i+1
    if(flag==1):
        print("Not prime")
        
    else:
        print("Prime")
        while(no!=0):
            rem=no%10
            sum=sum+rem
            no=no/10
        no=no+1
        print("Sum =",sum)
        return sum
prime(11)'''

#Super Prime
'''no=int(input("Enter no "))
def prime(no):
    for i in range(2,no):
        if(no%i==0):
            return False
    else:
        return True
x=prime(no)
if(x==True):
    print("Prime")
    if(no>9):
        sum=0
        for i in str(no):
            sum=sum+int(i)
        x=prime(sum)
        if(x==True):
            print("Super Prime")
        else:
            print("Not Super Prime")'''

#Function with fixed argument
'''
def person(name,age=18):
    print(name,age)
person("Shraddha",17)
person("Ram")'''

#Function with Infinite argument 
'''def add(*a):
    print(a)
    i=0
    sum=0
    for i in a:
        if(type(i)==tuple or type(i)==list):
            for j in i:
                if(type(j)==tuple or type(j)==list):
                    for k in j:
                        sum=sum+k
                else:
                    sum=sum+j
        else:
            sum=sum+i
    print("Addition =",sum)
add([20,30,40],[50,60,(90,40,50),33,44],40,40)'''

# function  marks([marks],[marks],[],[],[],[]) for 6 student

'''def person(**a):
    for i in a:
        print(i,"=",a[i],end=" ")
        print()
person(name="shraddha",company="Amplifier",Designation="Engineer",mobile_no=9657852656,city="Satara",pin_no= 415511)'''

#marks
'''
def mark(*m):
    for i in m:
        if(type(i)==list):
            sum=0
            flag=0
            for j in i:
                sum=sum+j
                per=sum/5
                if(j<35):
                    flag=flag+1
        print("Sum =",sum)
        per=sum/5
        print("Percentage =",per)
        if(flag==1 or flag==2):
            print("ATKT")
        elif(flag>=3):
            print(" Fail")
        elif(per>=50 and per<60):
            print("Seconnd class")
        elif(per>=60 and per<75):
            print("First  class")
        elif(per>=75 and per<=100):
            print("Distinction")
mark([12,53,94,56],[91,92,33,82],[99,88,77,99],[99,99,99,99],[98,78,90,89],[89,90,98,78])


'''

def mark(**m):
    for i in m:
        if(type(m[i])==list):
            max=0
            sum=0
            mar=0
            mar=sum
            for j in m[i]:
                sum=sum+j
                if(sum>mar):
                    max=i
                    per=sum/5
        print("Sum =",sum)
        per=sum/5
        print("Percentage =",per)
        if(per<35):
            print("Fail")
        elif(per>=40 and per<50):
            print(" Pass Only")
        elif(per>=50 and per<60):
            print("Seconnd class")
        elif(per>=60 and per<75):
            print("First  class")
        elif(per>=75 and per<=100):
            print("Distinction")
    print(max,"Congrullation!!!!")
    print("You are Topper!!!")

mark(Shraddha=[12,53,94,56],Rutika=[91,92,33,82],Pranita=[99,88,77,99],Siya=[99,99,99,99],Tanuja=[98,78,90,89],Nisha=[89,90,98,78])








