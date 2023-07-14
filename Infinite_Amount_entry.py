total=0        
while(1):
    amount=int(input("Enter a amount ="))
    total=total+amount
    state=input("Do you want to continue")
    if(state=="No"):
        break;
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
    print("Total amount =",total_am)'''
