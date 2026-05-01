print()
num = float(input("Enter a number: "))
check = lambda x: "Negative" if x<0 else "Positive" if x>0 else "Zero"
print(f'{num} is a {check(num)} number.')
print()