print("Welcome to Cloths Shop")
print("==================================")
print("*************ROYAL SHOP***********")
print("==================================")
print("Welcome to our shop!!!")
print("Select Section = \n1: Ladies \n2: Male")
a=int(input("Enter a Section Which Do you have ="))
if(a==1):
    print("You can Select the Ladies Section!!!")
    print("Please Go on First Floor!!!")
    print("Which type of clothes doy you have?")
    print("Select Section = \n1: Kurta \n2: Saree \n3: jeans \n4: Ghagra ")
    b=int(input("Enter Which type of Clothes do you have ="))
    if(b==1 or b==2 or b==3 or b==4):
        if(b==1):
            print("You selected :Kurta")
            print("Sections= \n1:simple \n2:Designer \n3: Plane")
            k=int(input("Which type of kurta you have??"))
            if(k==1):
                print("You selected:Simple Kurta")
            elif(k==2):
                print("You selected:Designer Kurta")
            elif(k==3):
                print("You selected:Plane Kurta")
        elif(b==2):
            print("You selected : Saree")
            print("Sections= \n1:Paithani \n2:Designer \n3:Wastern")
            s=int(input("Which type of saree you have??"))
            if(s==1):
                print("You select Paithani!!!")
            elif(s==2):
                print("You select Designer Saree!!!")
            elif(s==3):
                print("You select Wastern saree!!!")
        elif(b==3):
            print("You Selected :Jeans")
            print("Sections= \n1:simple \n2:Plane \n3: Shorts")
            j=int(input("Which type of jeans you have??"))
            if(j==1):
                print("You select Simple Jeans!!!")
            elif(j==2):
                print("You select Plane jeans!!!")
            elif(j==3):
                print("You select Short Jeans!!!")
        elif(b==4):
            print("You Selected Ghagra")
            print("Sections= \n1:Simple \n2:Designer")
            g=int(input("Which type og ghagra you have??"))
            if(g==1):
                print("You select Simple Ghagra!!!")
            elif(g==2):
                print("You select Designer Ghagra!!!")
        print("Which Size Do you have?")
        print("select = \n1:M \n2:L \n3:Xl \n4:2XL")
        c=int(input("Enter Size Dou you have ="))
        if(c==1 or c==2 or c==3 or c==4):
            if(c==1):
                print("You select Medium Size!!!")
            elif(c==2):
                print("You select Large Size!!!")
            elif(c==3):
                print("You select XL Size!!!")
            elif(c==4):
                print("You select 2Xl SIze")
            print("Which brand do you have ?")
            print("Select = \n1: Cottonking \n2:Zara \n3:Chanel \n4:Burbery ")
            d=int(input("Enter a brand do you have ="))
            if(d==1 or d==2 or d==3 or d==4):
                if(d==1):
                    print("You Select CottonKing Brand")
                elif(d==2):
                    print("You Select Zara Brand")
                elif(d==3):
                    print("You Select Chanel Brand")
                elif(d==4):
                    print("You Select Burbery Brand")
                print("Which type of pattern dou you have = ")
                print("select = \n1:Full sleeves \n2: Half Sleeves \n3:Half Shoulder ")
                e=int(input("Enter a Pattern type dou you have ="))
                if(e==1 or e==2 or e==3 or e==4):
                    if(e==1):
                        print("You Select Full Sleeves")
                    elif(e==2):
                        print("You Select Half Sleeves")
                    elif(e==3):
                        print("Which Colour do you have ??")
                    print("select = \n1: Red \n2:White \n3: Pink \n4: Black")
                    f=int(input("Enter a Colour do you have ="))
                    if(f==1 or f==2 or f==3 or f==4):
                        if(f==1):
                            print("You Select Red Colour")
                        elif(f==2):
                            print("You Select White Colour")
                        elif(f==3):
                            print("You Select Pink Colour")
                        elif(f==4):
                            print("You select Black colour")
                        print("************************************")
                        print("You Selected Sections =")
                        print("************************************")
                        print("Sections = \n1:Male \n2: Ladies")
                        if(a==1):
                            print("You Selected Ladies")
                        elif(a==2):
                            print("You Selected Male")  
                        print("Type of Cloths = \n1:Kurta \n2:Saree \n3:jeans \n4:Gbagra")
                        if(b==1):
                            print("You selected :Kurta")
                            print("Sections= \n1:simple \n2:Designer \n3: Plane")
                           # k=int(input("Which type of kurta you have??"))
                            if(k==1):
                                print("You selected:Simple Kurta")
                            elif(k==2):
                                print("You selected:Designer Kurta")
                            elif(k==3):
                                print("You selected:Plane Kurta")
                        elif(b==2):
                            print("You selected : Saree")
                            
                            if(s==1):
                                print("You select Paithani!!!")
                            elif(s==2):
                                print("You select Designer Saree!!!")
                            elif(s==3):
                                print("You select Wastern saree!!!")
                        elif(b==3):
                            print("You Selected :Jeans")
           # j=int(input("Which type of jeans you have??"))
                            if(j==1):
                                print("You select Simple Jeans!!!")
                            elif(j==2):
                                print("You select Plane jeans!!!")
                            elif(j==3):
                                print("You select Short Jeans!!!")
                        elif(b==4):
                            print("You Selected Ghagra")
            #g=int(input("Which type og ghagra you have??"))
                            if(g==1):
                                print("You select Simple Ghagra!!!")
                            elif(g==2):
                                print("You select Designer Ghagra!!!")
                        print("select Size = \n1:M \n2:L \n3:Xl \n4:2XL")
                        if(c==1):
                            print("You select Medium Size!!!")
                        elif(c==2):
                            print("You select Large Size!!!")
                        elif(c==3):
                            print("You select XL Size!!!")
                        elif(c==4):
                            print("You select 2Xl SIze") 
                        print("Select Brand = \n1: Cottonking \n2:Zara \n3:Chanel \n4:Burbery ")
                        if(d==1):
                            print("You Select CottonKing Brand")
                        elif(d==2):
                            print("You Select Zara Brand")
                        elif(d==3):
                            print("You Select Chanel Brand")
                        elif(d==4):
                            print("You Select Burbery Brand")
                        print("select sleeves pattern = \n1:Full sleeves \n2: Half Sleeves \n3:Half Shoulder ")
                        if(e==1):
                            print("You Select Full Sleeves")
                        elif(e==2):
                            print("You Select Half Sleeves")
                        elif(e==3):
                            print("You Select half Shoulder")
                        print("Which Colour do you have ??")
                        print("select colour = \n1: Red \n2:White \n3: Pink \n4: Black")
                        if(f==1):
                            print("You Select Red Colour")
                        elif(f==2):
                            print("You Select White Colour")
                        elif(f==3):
                            print("You Select Pink Colour")
                        elif(f==4):
                            print("You select Black colour")
                        print("You can Pay Bill on Counter!!!")
                        print("You can pay by online on QR Code!!!")
                        print("You can pay biil also by cash!!!")
                        print("Thank you for visit!!!!")
                        print("GOOD LUCK!!!")
                        print("************************************")
                        print("         Thank You                  ")
                        print("************************************")
                       
                    else:
                        print("Sorry!!!We dont have colour that you have Selected.Please choose another colour")
                else:
                    print("Sorry!!!We dont have pattern that you have Selected.please choose another pattern")
            else:
                print("Sorry!!!We dont have brand that you have Selected.please choose another brand")
        else:
            print("Sorry!!!We dont have Size that you have Selected.please choose another Size")
    else:
        print("Sorry!!!We dont have Section that you have Selected..please choose another Section")



elif(a==2):
    print("You can Select the Male Section!!!")
    print("Please Go on First Floor!!!")
    if(a==1):
        print("You Selected ladies")
    elif(a==2):
        print("You Selected MAle")
    print("Which type of clothes doy you have?")
    print("Select Section = \n1:Casual \n2: Formal \n3:T Shirts \n4:Sports ")
    b=int(input("Enter Which type of Clothes do you have ="))
    if(b==1 or b==2 or b==3 or b==4):
        if(b==1):
            print("You selected :Casual")
        elif(b==2):
            print("You selected : Formal")
        elif(b==3):
            print("You Selected :T shirts")
        elif(b==4):
            print("You Selected :Sports ")
        print("Which Size Do you have?")
        print("select = \n1:M \n2:L \n3:Xl \n4:2XL")
        c=int(input("Enter Size Dou you have ="))
        if(c==1 or c==2 or c==3 or c==4):
            if(c==1):
                print("You select Medium Size!!!")
            elif(c==2):
                print("You select Large Size!!!")
            elif(c==3):
                print("You select XL Size!!!")
            elif(c==4):
                print("You select 2Xl SIze")
            print("Which brand do you have ?")
            print("Select = \n1: Cottonking \n2:Zara \n3:Chanel \n4:Burbery ")
            d=int(input("Enter a brand do you have ="))
            if(d==1 or d==2 or d==3 or d==4):
                if(d==1):
                    print("You Select CottonKing Brand")
                elif(d==2):
                    print("You Select Zara Brand")
                elif(d==3):
                    print("You Select Chanel Brand")
                elif(d==4):
                    print("You Select Burbery Brand")
                print("Which type of pattern dou you have = ")
                print("select = \n1:Full sleeves \n2: Half Sleeves \n3:Half Shoulder ")
                e=int(input("Enter a Pattern type dou you have ="))
                if(e==1 or e==2 or e==3 or e==4):
                    if(e==1):
                        print("You Select Full Sleeves")
                    elif(e==2):
                        print("You Select Half Sleeves")
                    print("Which Colour do you have ??")
                    print("select = \n1: Red \n2:White \n3: Pink \n4: Black")
                    f=int(input("Enter a Colour do you have ="))
                    if(f==1 or f==2 or f==3 or f==4):
                        if(f==1):
                            print("You Select Red Colour")
                        elif(f==2):
                            print("You Select White Colour")
                        elif(f==3):
                            print("You Select Pink Colour")
                        elif(f==4):
                            print("You select Black colour")
                        print("************************************")
                        print("You Selected Sections =")
                        print("************************************")
                        print("Sections = \n1:Male \n2: Ladies")
                        if(a==1):
                            print("You Selected Male")
                        elif(a==2):
                            print("You Selected MAle")
                        print("Type of Cloths = \n1:Casual \n2:Formal \n3:T Shirts \n4:Sports")
                        if(b==1):
                            print("You selected :Casual")
                        elif(b==2):
                            print("You selected : Formal")
                        elif(b==3):
                            print("You Selected :T shirts")
                        elif(b==4):
                            print("You Selected :Sports ")
                        print("select Size = \n1:M \n2:L \n3:Xl \n4:2XL")
                        if(c==1):
                            print("You select Medium Size!!!")
                        elif(s==2):
                            print("You select Large Size!!!")
                        elif(s==3):
                            print("You select XL Size!!!")
                        elif(s==4):
                            print("You select 2XL Size!!!")

                        print("Select Brand = \n1:Cottonking \n2:Zara \n3:Chanel \n4:Burbery ")
                        if(d==1):
                            print("You Select CottonKing Brand")
                        elif(d==2):
                            print("You Select Zara Brand")
                        elif(d==3):
                            print("You Select Chanel Brand")
                        elif(d==4):
                            print("You Select Burbery Brand")
                        print("select sleeves pattern = \n1:Full sleeves \n2: Half Sleeves ")
                        if(e==1):
                            print("You Select Full Sleeves")
                        elif(e==2):
                            print("You Select Half Sleeves")
                        print("select colour = \n1: Red \n2:White \n3: Pink \n4: Black")
                        if(f==1):
                            print("You Select Red Colour")
                        elif(f==2):
                            print("You Select White Colour")
                        elif(f==3):
                            print("You Select Pink Colour")
                        elif(f==4):
                            print("You select Black colour")
                        print("You can Pay Bill on Counter!!!")
                        print("You can pay by online on QR Code!!!")
                        print("You can pay biil also by cash!!!")
                        print("Thank you for visit!!!!")
                        print("GOOD LUCK!!!")
                        print("************************************")
                        print("         Thank You                  ")
                        print("************************************")
                       
                    else:
                        print("Sorry!!!We dont have colour that you have Selected.Please choose another colour")
                else:
                    print("Sorry!!!We dont have pattern that you have Selected.please choose another pattern")
            else:
                print("Sorry!!!We dont have brand that you have Selected.please choose another brand")
        else:
            print("Sorry!!!We dont have Size that you have Selected.please choose another Size")
    else:
        print("Sorry!!!We dont have Section that you have Selected..please choose another Section")
