marks=int(input("Enter a marks ="))
if(marks>45):
    print("Pass")
    if(marks>=50):
        print("Second class")
        if(marks>=60):
            print("1st class")
            if(marks>=75):
                print("Distinction")
else:
    print("Fail")
