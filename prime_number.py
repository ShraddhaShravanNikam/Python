no=0
while(no<100):
    no=no+1
    i=2
    flag=0 
    while(i<no):
        if(no%i==0):
            flag=1
            break
        i=i+1
    if(flag==1):
        print("Not Prime =",no)
    else:
       print("Prime =",no)'''
       

