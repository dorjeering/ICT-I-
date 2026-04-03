print()
userDetails={'Id':1, 'userName':'Just_Me'} #Creating a dictionary with user details
print(type(userDetails)) #Checking the type of the variable userDetails
print(userDetails)
location=dict(s='Samtse', t='Thimphu',p='Paro')
print(type(location))#Checking the type of the variable location
print(location)
print(location['s']) #Accessing the value of key 's' in the location dictionary
print(location.get('t')) #Accessing the value of key 't' in the location dictionary using get() method
location['b']='Bumthang' #Adding a new key-value pair to the location dictionary
print(location)
userDetails['email']='justme@example.com' #Adding a new key-value pair to the userDetails dictionary
print(userDetails)
userDetails['userName']='Just_Me_Updated' #Updating the value of the existing key 'userName' in the userDetails dictionary
print(userDetails)
del location['p'] #Deleting the key-value pair with key 'p' from the location dictionary
print(location)
dv=userDetails.pop('email') #Removing the key-value pair with key 'email' from the userDetails dictionary and storing the value in variable dv
print(dv) 
del_key, del_value=userDetails.popitem() #Removing the last inserted key-value pair from the userDetails dictionary and storing the key and value in variables del_key and del_value
print(f'the deleted key is {del_key} and the deleted value is {del_value}')#Printing the deleted key and value
location.clear() #Clearing all key-value pairs from the location dictionary
print(location) #Printing the empty location dictionary
print()