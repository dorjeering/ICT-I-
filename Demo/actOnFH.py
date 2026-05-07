file = open('Students.csv', 'w')
file.write("Name, ID\n")
file.write("Dorji, 001\n")
file.write("Karma, 002\n")
file.write("Sonam, 003\n")
file.write("Tashi, 004\n")
file.close()
file = open('Students.csv', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.csv', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()