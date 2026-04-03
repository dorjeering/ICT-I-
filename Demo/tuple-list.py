print()
mt = ("Hello", 123456)#creating a tuple
print(type(mt)) #creating a tuple
print(mt) #accessing tuple elements
print(mt[1])
a,b=mt #unpacking
print(b) #converting tuple to list
nt=tuple(a) #converting string to tuple
print(nt)
concatenatedt=mt+nt #concatenating tuples
print(concatenatedt)#slicing
print(concatenatedt[2:6:2]) #reversing a tuple
print(concatenatedt[::-1]) #deleting a tuple
print(concatenatedt[:2]+concatenatedt[2:][::-1])#reversing a tuple from index 2 to end
n = concatenatedt[2:7:4] #slicing a tuple from index 2 to end with step 4
print(n[::-1]) #reversing a tuple from index 2 to end with step 4
print(concatenatedt[2:7:4][::-1]) #reversing a tuple from index 2 to end with step 4
print(concatenatedt[6:1:-4]) #slicing a tuple from index 6 to index 1 with step -4
print(concatenatedt[::-4]) #reversing a tuple with step -4