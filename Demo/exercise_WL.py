print("<<>><<>>"*15)
countdown_timer = 10
while countdown_timer > 0:
    print(countdown_timer)
    countdown_timer -= 1
print("Time's up!")
print("<<>><<>>"*15)
num = int(input("Enter number to calculate the sum: "))
sum = 0
while num > 0:
    sum += num
    num = int(input("Enter number to calculate the sum: "))
print("The sum is: ", sum)
print("<<>><<>>"*15)
for i in range(3):
    username = input("Enter your username: ")
    if username == "admin":
        break
    else:
        print(f'Attempt {i+1}: Invalid username')
else:
    print("Too many attempts! Account locked.")
    exit()
for i in range(3):
    password = input("Enter your password: ")
    if password == "1234":
        print("Login Successful")
        print("Welcome, Admin")
        break
    else:
        print(f'Attempt {i+1}: Invalid password')
else:
    print("Too many attempts! Account locked.")
print("<<>><<>>"*15)