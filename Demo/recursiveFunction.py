#sum of natural numbers using recursion
print()
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n - 1)
n = int(input("Enter a number: "))
print("The sum of numbers from 1 to {} is: {}".format(n, sum(n)))
print()
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n - 1)
n = int(input("Enter a number: "))
print("Factorial of {} is: {}".format(n, fact(n)))
print()