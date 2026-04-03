print()
userDetails={'Id':1, 'userName':'Just_Me'} #Creating a dictionary with user details
print(type(userDetails)) #Checking the type of the variable userDetails
print(userDetails)
location=dict(s='Samtse', t='Thimphu',p='Paro')
print(type(location))#Checking the type of the variable location
print(location)
print(location['s']) #Accessing the value of key 's' in the location dictionary
print(location.get('t')) #Accessing the value of key 't' in the location dictionary using get() method
print(location.get('d')) #Trying to access a non-existent key 'd' in the location dictionary using get() method with a default value
location['b']='Bumthang' #Adding a new key-value pair to the location dictionary
print(location)
userDetails['email']='justme@example.com' #Adding a new key-value pair to the userDetails dictionary
print(userDetails)
userDetails['userName']='Just_Me_Updated' #Updating the value of the existing key 'userName' in the userDetails dictionary
print(userDetails)
print()