courses = []

def add_course():
    title = input("Course title: ")
    try:
        duration = int(input("Duration (hours): "))
        enrolled = int(input("Enrolled students: "))
        courses.append({'title': title, 'duration': duration, 'enrolled': enrolled})
    except: print("Invalid input.")

def update_enrolled():
    title = input("Course title to update: ")
    for c in courses:
        if c['title'].lower() == title.lower():
            try:
                c['enrolled'] = int(input("New enrolled number: "))
                print("Updated.")
                return
            except: print("Invalid number.")
    print("Course not found.")

def filter_duration():
    try:
        duration = int(input("Minimum duration: "))
        for c in courses:
            if c['duration'] >= duration:
                print(c)
    except: print("Invalid input.")

def menu():
    while True:
        print("\n1. Add course\n2. Update enrolled\n3. Filter by duration\n4. Exit")
        op = input("Option: ")
        if op == '1': add_course()
        elif op == '2': update_enrolled()
        elif op == '3': filter_duration()
        elif op == '4': break
        else: print("Invalid option.")

menu()