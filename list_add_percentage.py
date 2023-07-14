#list Addition

m=[[20,30,40,50],[20,10,40,50],[10,20,30,40],[10,20,30,40]]
i=0
while(i<len(m)):
    j=0
    s=0
    while(j<len(m[i])):
        s=s+m[i][j]
        j=j+1
    print("Sum=",s)
    per=s/5;
    print("Percentage =",per)
    if(per>40 and per<50):
        print("Pass")
    elif(per>50 and per<60):
        print("2nd class")
    elif(per>60 and per<75):
        print("1st class")
    elif(per>75 and per<=100):
        print("Distinction")
    else:
        print("Fail")
    i=i+1
