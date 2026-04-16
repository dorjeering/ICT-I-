print("====="*24)
no_of_student = int(input("Enter the number of students: ")) #taking input for number of students to be added to the list of students
i = 1
student_names = {}
while i <= no_of_student: #setting the condition for the while loop to be executed until the value of i is less than or equal to the number of students
    name = input("Enter the name of student: ")
    print("The name of student {} is {}".format(i,name))
    i += 1 #incrementing the value of i by 1 in each iteration of the while loop
    student_names[i] = name #adding the student name to the dictionary with the key as the value of i and the value as the student name
print("The list of students is: ", student_names) #printing the list of students after adding the student names to the dictionary
print()
while True:
    print("This is an infinite loop. Press Ctrl+C to stop it.") #printing the message for the infinite loop
print("====="*24)

#Loop Control Statements
print()
for i in range(4):
    if i == 2:
        break #using break statement to exit the loop when the value of i is equal to 2
    print(i)
for i in range(4):
    if i == 2:
        continue #using continue statement to skip the rest of the code in the loop when the value of i is equal to 2 and move to the next iteration of the loop
    print(i)
print("Loop Ended")
print("<<>><<>>"*15)