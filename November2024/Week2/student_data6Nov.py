def calculate_grade(total_marks):
    if mark >=90:
        return 'A'
    elif mark >=82:
        return 'B'
    elif mark >=75:
        return 'C'
    elif mark >=60:
        return 'D'
    elif mark >=50:
        return 'P'
    else:
        return 'F'

name = input("Enter student's name: ")
roll_number = int(input("Enter roll number: "))
register_number = input("Enter register number: ")
department = input("Enter department: ")
semester = int(input("Enter semester: "))

student_details = {
    'name': name,
    'roll_number': roll_number,
    'register_number': register_number,
    'department': department,
    'semester': semester,
}
print("Entered student details:", student_details)

total_marks = int(input("Enter total marks: "))
student_details['total_marks'] = total_marks

grade = calculate_grade(total_marks)
student_details['grade'] = grade

print("\nUpdated student details : ",student_details)

del student_details['roll_number']

print("\nStudent details after rollno deletion: ",student_details)
