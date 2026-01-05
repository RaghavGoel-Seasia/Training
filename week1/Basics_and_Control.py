student_data = {}
templist = []

# Allowed characters for names
valid_chars = "abcdefghijklmnopqrstuvwxyz .'-"


def feed():
    print("Enter students. Leave name empty to stop.")


    while True:
        name = input("Enter student name: ").strip()

        # Purging double whitespaces in name
        while "  " in name:
            name = name.replace("  "," ")

        if not name:
            break  # stop when user enters a blank name


        # Check name has only allowed characters
        ok = True
        for ch in name.lower():
            if ch not in valid_chars:
                ok = False
                break

        if not ok:
            print("Invalid name. Use letters/spaces/dot/hyphen/apostrophe.")
            continue

        # Fix capitalisation (title case)
        name = name.title()

        # Create the student entry if it doesn't exist
        if name not in student_data:
            student_data[name] = []

        # Keep taking grades until user leaves it blank
        while True:
            grade_input = input("Enter grade for " + name + " (blank to stop): ").strip()
            if not grade_input:
                break

            try:
                grade = float(grade_input)
                if abs(grade) == float('inf'):
                        raise ValueError
                student_data[name].append(round(grade, 2))
            except ValueError:
                print("That wasn't a number. Try again.")

        print("Current data:", student_data)

    print("\nFinal Student Data:")
    for name, grades in student_data.items():
        # Avoid dividing by zero if there are no grades
        if len(grades) > 0:
            avg = sum(grades) / len(grades)
        else:
            avg = 0.0

        print(name, "| Grades:", grades, "| Average:", round(avg, 2))

feed()
