print()#printing an empty line for better readability
student_list = [] #creating an empty list
student_age = set()#creating an empty set
student_grade = set()#creating an empty set
student_dict = {}#creating an empty dictionary

student_list.append("Dorji")#adding student name to the list
student_list.append("Tshering")#adding student name to the list
student_list.append("Karma")#adding student name to the list
student_list.append("Wangdi")#adding student name to the list
student_age.add(20)#adding student age to the set
student_age.add(21)#adding student age to the set
student_age.add(22)#adding student age to the set
student_age.add(23)#adding student age to the set
student_grade.add('A')#adding student grade to the set
student_grade.add('A')#adding student grade to the set
student_grade.add('A')#adding student grade to the set
student_grade.add('A')#adding student grade to the set
student_dict['Dorji'] = {'age': 20, 'grade': 'A'}#adding student details to the dictionary
student_dict['Tshering'] = {'age': 21, 'grade': 'A'}#adding student details to the dictionary
student_dict['Karma'] = {'age': 22, 'grade': 'A'}#adding student details to the dictionary
student_dict['Wangdi'] = {'age': 23, 'grade': 'A'}#adding student details to the dictionary
print("Existing students: ", student_list) #printing the existing list of students
print()#printing an empty line for better readability

add_student = input("Enter the student name to add or else enter to skip: ") #taking input for student name to be added to the existing list of students
add_age = int(input("Enter the age of the student: ")) #taking input for student age to be added to the existing set of student ages and also to be added to the dictionary along with the student name
add_grade = input("Enter the grade of the student: ") #taking input for student grade to be added to the existing set of student grades and also to be added to the dictionary along with the student name
if add_student: #checking if the input for student name
    student_list.append(add_student) #adding student name to the list
    student_age.add(add_age) #adding student age to the set
    student_grade.add(add_grade) #adding student grade to the set
    student_dict[add_student] = {'age': add_age, 'grade': add_grade} #adding student details to the dictionary 
    print(f"Student added successfully! The age of the student '{add_student}' is {student_dict[add_student]['age']} and the grade is {student_dict[add_student]['grade']}.")#printing the details of the new student added before
    print("Updated list of students with their details: ", student_dict) #printing the new list of students after adding the new student to the existing list of students
else:
    print("No student added")#printing the reminder if no student are added
print()#printing a blank line
search_name = input("Enter the student name to search: ")#taking input for student name to be searched in the existing list of students and also to be searched in the dictionary to get the details of the particular student if found
if search_name in student_list: #checking if the input for student name is there in the existing list of students
    print(f"Student found! The age of the student '{search_name}' is {student_dict[search_name]['age']} and the grade is {student_dict[search_name]['grade']}.") #printing the details of the student if found in the list and in the dictionary
else: #another condition to be executed if the first condition is not satisfied
    print("Student not found")#printing the reminder if the student is not found in the list and in the dictionary
print()#printing a blank line
remove_student = input("Enter the student name to remove or else enter to skip: ")#taking input for student name to be removed from the existing list of students and also to be removed from the dictionary along with the details of the particular student if found
if remove_student in student_list: #checking if the input for student name is there in the existing list of students or not
    remove_age = student_dict[remove_student] #getting the age of the student to be removed from the dictionary before removing the student from the list and from the dictionary
    remove_grade = student_dict[remove_student] #getting the grade of the student to be removed from the dictionary before removing the student from the list and from the dictionary
    student_list.remove(remove_student) #removing student name from the list
    del student_dict[remove_student] #removing student details from the dictionary

    print("Student removed successfully!") #printing the message of success if the student is removed successfully
    print()
    print("Students left along with their details: ", student_dict) #printing the details of the remaining students after removing the particular student from the dictionary
    print()
    print("List of students left: ", student_list) #printing the list of remaining students after removing the particular student from the list
else: #setting the second condition to be executed if the first condition is not satisfied
    print("Student not found") #printing the message of successfully excuting the second condition
print()#printing a blank line