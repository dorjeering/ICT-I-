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
tup = ("John Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)
set1 = {10,30,20}
for x in set1:
    print(x)
print()