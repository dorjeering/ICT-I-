print()
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

add_student = input("Enter the student name to add or else enter to skip: ")
add_age = int(input("Enter the age of the student: "))
add_grade = input("Enter the grade of the student: ")
if add_student:
    student_list.append(add_student)
    student_dict[add_student] = {'age': add_age, 'grade': add_grade}
    print(f"Student added successfully! The age of the student '{add_student}' is {student_dict[add_student]['age']} and the grade is {student_dict[add_student]['grade']}.")
else:
    print("No student added")

search_name = input("Enter the student name to search: ")
if search_name in student_list:
    print(f"Student found! The age of the student '{search_name}' is {student_dict[search_name]['age']} and the grade is {student_dict[search_name]['grade']}.")
else:
    print("Student not found")

remove_student = input("Enter the student name to remove or else enter to skip: ")
if remove_student in student_list:
    remove_age = student_dict[remove_student]
    remove_grade = student_dict[remove_student]
    student_list.remove(remove_student)
    del student_dict[remove_student]

    print("Student removed successfully!")
    print("Students left along with their details: ", student_dict)
    print("List of students left: ", student_list)
else:
    print("Student not found")
print()