print()
name = input("Enter your name: ")
for i in name:
    print(i)
print()
li = ["Python Programming", "Python Fundamentals","Python Interview Questions"]
for x in li:
    print(x)
print()
lenli = len(li)
for x in range(lenli):
    print(li[x])
print()

tl = tuple(li)
for x in tl:
    print(x)
print()
lentl = len(tl)
for x in range(lentl):  
    print(tl[x])
print()

sl = set(li)
for x in sl:
    print(x)
print()
