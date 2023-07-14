age=int(input("Enter age = "))
if(age>18):
    print("Elligible for vote ")
    voter_id =input("Do you have voter id = ")
    if(voter_id=='yes'):
        print("You can Vote ")
    else:
        print("You cannot vote")
else:
     print("Not Elligible for vote ")
