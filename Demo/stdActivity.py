print()
print("====="*10)
n = input("Name: ")
ndbb = int(input("Enter the number of days the book was borrowed: "))
ndbl = int(input("Enter the number of days late to return: "))    
if ndbl<=0:
    print("you have no due.")
    print("Keep it up.👍")
elif ndbl<=5:
    f= (ndbl * 5)
    print("You have a total fine of Nu.",f, " to pay.")
elif ndbl<=10:
    fi=(ndbl*10)
    print("You have a total fine of Nu.",fi," to pay.")
else:
    fin=(ndbl*20)
    print("you have a total fine of Nu.",fin,"/- to pay.")
if ndbl>=30:
    print("WARNING☠️ : Library privileges may be restricted.")
    print("Please return or get duration extension on time.")
else:
    pass
print("====="*10)
print()