print()
def fun(x,y):
    if x==0:
        return y
    else:
        return fun(x-1,y+x)
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
print("The value of fun({}, {}) is: {}".format(x,y,fun(x,y)))
print()