i=int(input("Enter a range of product  ="))
j=0
k=1
total=0
dis=0
total_am=0
while(j<i):
    print("Product ",k)
    amount=int(input("Enter a amount of product ="))
    k=k+1
    j=j+1
    total=total+amount
    print("Total amount =",total)
if(total>=5000 and total<=10000):
    print("You have 3% discount ")
    dis=total*0.03
    print("Discount =",dis)
    total_am=total-dis
    print("Total amount =",total_am)
elif(total>=10000 and total<=15000):
    print("You have 3% discount ")
    dis=total*0.05
    print("Discount =",dis)
    total_am=total-dis
    print("Total amount =",total_am)
elif(total>=15000 and total<=25000):
    print("You have 3% discount ")
    dis=total*0.07
    print("Discount =",dis)
    total_am=total-dis
    print("Total amount =",total_am)
    
