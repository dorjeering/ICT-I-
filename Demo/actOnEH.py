try:
    file = open("students.txt", "r")
    students = file.readlines()
except FileNotFoundError:
    print("File not found!")
except:
    print("An unexpected error occurred.")
else:
    for student in students:
        print(student.strip())
finally:
    print("Mission Accomplished.")
    if 'file' in locals():
        file.close()