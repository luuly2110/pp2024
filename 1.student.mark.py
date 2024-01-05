#function to input student's information
def input_student():
    student = []
    num_student = int(input("Enter the number of students: ")) 
    for i in range(num_student):
        print(f"Enter information of student #{i+1}: ") 
        id = input("ID: ")
        name = input("Name: ")
        dob = input("Date of birth: ")

        new_student = {'Id': id, 'Name': name, 'Dob': dob, 'Mark': {}}
        student.append(new_student)     #add new student to the list

    return student

#function to input course's information
def input_course():
    course = []
    num_course = int(input("Enter the number of courses: "))
    for i in range(num_course):
        print(f"Enter information of course #{i+1}: ")
        id = input("ID: ")
        name = input("Name: ")

        new_course = {'Id': id, 'Name': name}
        course.append(new_course)       #add new course to the list

    return course 

#function to input mark's information
def input_mark(student, course):
    course_id = input("Enter the course's id to input marks: ")
    for c in course:
        if c['Id'] == course_id:
            print(f"Entering marks for the course: {c['Name']}")
            for s in student:
                mark = float(input(f"Enter mark for student {s['Name']} (ID: {s['Id']}): "))
                s['Mark'][course_id] = mark

#function to list student's information
def list_student(student):
    print("List of students: ")
    for s in student:
        print(f"ID: {s['Id']}, Name: {s['Name']}, DoB: {s['Dob']}")

#function to list course's information
def list_course(course):
    print("List of courses: ")
    for c in course:
        print(f"ID: {c['Id']}, Name: {c['Name']}")

#function to show marks
def show_mark(student):
    course_id = input("Enter the course's id to show marks: ")
    for s in student:
        if course_id in s['Mark']:
            print(f"Student {s['Name']} (ID: {s['Id']}) has mark: {s['Mark'][course_id]}")

#main program
student = input_student()
course = input_course()
input_mark(student, course)
list_student(student)
list_course(course)
show_mark(student)




