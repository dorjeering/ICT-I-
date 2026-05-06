print()
while True:
    name = input("Enter your name: ")
    if not name:
        break
    if name == 'exit':
        print("GOODBYE...")
        break
    greet = lambda x: print("Hello, ", x)
    greet(name)
print()
print("x=x=x=x="*14,"x")
print()
even_odd = lambda x: "Even" if x%2 == 0 else "Odd"
num = int(input("Enter a number: "))
print(f'{num} is {even_odd(num)} number.')
print()
print("x=x=x=x="*14,"x")
print()
arith = lambda x, y: (x+y, x-y, x*y, x/y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(arith(num1, num2))
print()
print("x=x=x=x="*14,"x")
print()
mlist = [1,2,3,4,5,6]
even = filter(lambda x: x%2 == 0 , mlist)
print("Even numbers in the list: ", list(even))
print()
print("x=x=x=x="*14,"x")
print()
nlist = [1,2,3,4]
double = map(lambda x: x*2, nlist)
newlist = list(double)
back = map(lambda x: x/2, newlist)
print("Doubled numbers: ", list(double))
print("Converting back to nlist: ", list(back))
print()
from functools import reduce
mlist = [1,2,3,4]
mul = reduce(lambda x, y: x*y, mlist)
print("Multiplication of all numbers in the list: ", mul)
print()