H = float(input("Enter height(m): "))
W = float(input("Enter weight: "))
BMI = W / (H**2)
print("Your BMI is:", BMI)
if BMI <18.5:
    print("You are underweight")
elif 18.5<BMI<24.5:
    print("You are normal")
else:
    print("You are overweight")