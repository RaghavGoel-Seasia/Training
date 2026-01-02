student_data = {}
alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '.']

def feed():
    print("Input student data. Leave name/marks blank to stop.")
    
    while True:
        # Prompt for student name
        name = input("Enter student name: ").strip()
        if not name:  # Exit if no name entered
            print("Exiting data entry.")
            break
        
        # Ensure the name only contains valid characters (letters and spaces)
        if not all(char.lower() in alphabets for char in name.replace(" ", "").lower()):
            print("Invalid name! Please use only letters and spaces.")
            continue

        # Capitalize first letters of each word in the name
        name = ' '.join([word.capitalize() for word in name.split()])

        # Collect grades for the student
        grades = []
        while True:
            grade_input = input(f"Enter grade for {name} (leave blank to stop): ").strip()
            if not grade_input:
                break  # Stop if no grade input
            
            try:
                grade = round(float(grade_input), 2)
                grades.append(grade)
            except ValueError:
                print("Invalid grade! Please enter a numeric value.")
                continue
        
        # Store the grades in the student data
        if grades:
            if name in student_data:
                student_data[name].extend(grades)  # Append grades for existing student
            else:
                student_data[name] = grades  # Add new student with their grades
        
        # Show current data
        print(f"Current data: {student_data}")
    
    # Final output: Display all student data with averages
    print("\nFinal Student Data:")
    for student, grades in student_data.items():
        avg_grade = sum(grades) / len(grades)  # Calculate average grade
        print(f"{student} | Grades: {grades} | Average: {round(avg_grade, 2)}")

feed()
