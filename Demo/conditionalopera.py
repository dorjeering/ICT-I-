m1 = float(input("Enter the marks of first subject: "))
m2 = float(input("Enter the marks of second subject: "))
m3 = float(input("Enter the marks of third subject: "))
avg = (m1+m2+m3)/3
print()
print("Average:%.2f " %(avg))
print()
if (avg>=90 and m1>=50 and m2>=50 and m3>=50):
    print("Grade A")
    print()
elif (avg>=80 and m1>=50 and m2>=50 and m3>=50):
    print("Grade B")
    print()
elif (avg>=70 and m1>=50 and m2>=50 and m3>=50):
    print("Grade C")
    print()
elif (avg>=60 and m1>=50 and m2>=50 and m3>=50):
    print("Grade D")
    print()
elif (avg>=50 and m1>=50 and m2>=50 and m3>=50):
    print("Grade E")
    print()
else:
    print("You need to work harder.")
    print() #for space after the condition is true.