from utils import (
    display_menu, 
    user_choice, 
    add_student, 
    view_students, 
    search_student
)

def main():
    while True:
        display_menu()
        choice = user_choice()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()

