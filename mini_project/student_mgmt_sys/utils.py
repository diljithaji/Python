import database 

def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for Student")
    print("4. Exit")
    print("---------------------------------")

def user_choice():
    choice = input("Enter your choice (1-4): ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please enter a number between 1 and 4.")
        choice = input("Enter your choice (1-4): ")
    return choice

def add_student():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")
    
    if database.search_student(student_id):
        print(f"Error: Student with ID {student_id} already exists.")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Student Course (e.g., AI, DS, MSC): ")
    
    new_student = {
        'id': student_id,
        'name': name,
        'course': course
    }
    
    database.add_student(new_student)
    print(f"Success: Student '{name}' added.")

def view_students():
    print("\n--- All Students ---")
    
    all_students = database.view_students()
    
    if not all_students:
        print("No students found in the database.")
    else:
        print(f"Total Students: {database.student_count()}")
        print("--------------------")
        for student in all_students:
            print(f"ID: {student['id']}\nName: {student['name']}\nCourse: {student['course']}")

def search_student():
    print("\n--- Search for Student ---")
    student_id = input("Enter Student ID to search: ")
    
    student = database.search_student(student_id)
    
    if student:
        print("--- Student Found ---")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
    else:
        print(f"No student found with ID: {student_id}")

