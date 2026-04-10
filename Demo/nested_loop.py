print("====="*24)
for i in range(1,4): # Outer loop iterates from 1 to 3
    for j in range(i): # Inner loop iterates from 0 to i-1
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j+1}") 
print("====="*24)
for i in range(4):
    for j in range(i):
        print("*", end=" ") 
    print()
print("====="*24)
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ") 
    print()
print("====="*24)
for i in range(6,0,-1):
    for j in range(1,i):
        print("$", end="🤣  ") 
    print()
print("====="*24)

'''for i in range(1):
    for j in range(1,i+3):
        print("*", end=" ")'''
for i in range(1):
    for j in range(1,i+3):
        print("*")
for f in range(1):
    for h in range(1,i+4):
        print("*", end=" ")
print()