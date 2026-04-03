print()
s = {1,2,3,"Hello",3.14,1,2,False} #creating a set
print(type(s)) #checking the type of s
print(s)
s.add("World") #adding an element to a set
print(s) #removing an element from a set
ss={3,4,5}
us=s.union(ss) #union of two sets
print(us)
ins=s.intersection(ss) #intersection of two sets
print(ins)
ds=s.difference(ss) #difference of two sets
print(ds)
dis=ss.difference(s) #difference of two sets
print(dis)
s.clear() #clearing a set
print(s) #deleting a set
print()