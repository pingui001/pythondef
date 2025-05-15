students = {}

def register_student():
    print("_________________________________________")
    print("--- REGISTER STUDENT ---")
    name = input("Enter the student's name: \n").strip()
    if name in students:
        print(f"The student '{name}' is already registered.")
    else:
        students[name] = []  # Start with empty grade list
        print(f"Student '{name}' has been registered successfully.")

def add_grades():
    print("_________________________________________")
    print("--- ADD GRADES ---")
    name = input("Enter the student's name: ").strip()
    if name in students:
        grades_input = input("Enter a list of grades (separated by commas):\n ")
        try:
            grades = [float(grade.strip()) for grade in grades_input.split(',')]
            students[name].extend(grades)
            print(f"Grades added for student '{name}'.")
        except ValueError:
            print("Error... Please enter only numbers separated by commas.")
    else:
        print(f"Student '{name}' is not registered.")

def view_students():
    print("__________________________________________")
    print("--- VIEW STUDENTS ---")
    if students:
        for name, grades in students.items():
            print(f"Student: {name}, Grades: {grades}")
    else:
        print("No students registered yet.")

def see_average():
    print("___________________________________________")
    print("--- SEE AVERAGE ---")
    name = input("Student name: \n").strip()
    if name in students:
        if students[name]:
            average = sum(students[name]) / len(students[name])
            print(f"{name}'s average: {average:.2f}")
        else:
            print(f"Student '{name}' has no grades yet.")
    else:
        print(f"Student '{name}' is not registered.")

def menu():
    print("\n1. Register student.")
    print("2. View students.")
    print("3. See student average.")
    print("4. Add grades.")
    print("5. Exit.")

def main():
    continue_program = True
    while continue_program:
        menu()
        try:
            selected_option = int(input("\n--- SELECT AN OPTION: "))
            if selected_option == 1:
                register_student()
            elif selected_option == 2:
                view_students()
            elif selected_option == 3:
                see_average()
            elif selected_option == 4:
                add_grades()
            elif selected_option == 5:
                print("--- Exiting the program. Goodbye!")
                continue_program = False
            else:
                print("--- Invalid option. Please select a valid number from the menu.")
        except ValueError:
            print("--- Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
