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
    mark = int(input("Enter Mark: "))

    student_details = {
        "name": name,
        "roll_no": roll_no,
        "register_no": register_no,
        "department": department,
        "semester": semester,
        "mark": mark,
    }
    
    grade  = cal_grade(mark)
    student_details['grade'] = grade
    return student_details
student_info = get_student_details()
print("student information :",student_info)
print("After Deleting Roll Number: ")
new_info = {key: value for key, value in student_info.items() if key != 'roll_no'}
print(new_info)
