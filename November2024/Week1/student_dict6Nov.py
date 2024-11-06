def cal_grade(mark):
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
    
def get_student_details():
    name = input("Enter student's name: ")
    roll_no = int(input("Enter roll number: "))
    register_no = input("Enter registration number: ")
    department = input("Enter department: ")
    semester = int(input("Enter semester: "))
    

    student_details = {
        "name": name,
        "roll_no": roll_no,
        "register_no": register_no,
        "department": department,
        "semester": semester,
        
    }
    return student_details
student_info = get_student_details()
print("\nStudent information :",student_info)

mark = int(input("\nEnter mark: "))
student_info['mark'] = mark

grade  = cal_grade(mark)
student_info['grade'] = grade


print("\nUpdated information :")
print("\nStudent information :\n",student_info)
print("\nAfter Deleting Roll Number:\n ")
new_info = {key: value for key, value in student_info.items() if key != 'roll_no'}
print(new_info)
