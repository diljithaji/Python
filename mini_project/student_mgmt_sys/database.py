students = []

def add_student(new_student):
    students.append(new_student)

def view_students():
    return students

def student_count():
    return len(students)

def search_student(student_id):
    searched_student = None
    for student in students:
        if student['id'] == student_id:
            searched_student = student
            break

    return searched_student

