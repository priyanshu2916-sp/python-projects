# ==========================================
# PROJECT 1: ATM SIMULATOR
# ==========================================

def atm_simulator():
    correct_pin = "1234"
    balance = 10000
    attempts = 3
    transactions = []

# Stage 1: PIN check
    while attempts > 0:
        pin = input("Enter your PIN: ")

        if pin == correct_pin:
            print("PIN correct!")
            break
        else:
            attempts -= 1

            if attempts > 0:
                print("Wrong PIN. Attempts left:", attempts)
            else:
                print("Card blocked.")
                return

# Stage 2, 3 and 4: Menu, Deposit and Withdraw, Extension
    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance:", balance)

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    transactions.append(("Deposit", amount))
                    print("New balance:", balance)
                else:
                    print("Amount must be above 0.")

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Amount must be above 0.")

                elif amount > balance:
                    print("Insufficient balance")

                else:
                    balance -= amount
                    transactions.append(("Withdraw", amount))
                    print("New balance:", balance)

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "4":
            print("Thank you!")
            print("\nTransaction History:")

            for transaction, amount in transactions:
                print(transaction, amount)

            break

        else:
            print("Invalid choice. Try again.")


# ==========================================
# PROJECT 2: STUDENT MARKS MANAGER
# ==========================================

def student_marks_manager():
    students = {
        "Aman": [85, 90, 78],
        "Riya": [92, 88, 95],
        "Zoya": [70, 65, 80]
    }

    def calculate_average(marks):
        return sum(marks) / len(marks)

    def calculate_grade(avg):
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

# Stage 1 and 2: Averages and Grades
    def view_all():
        for name, marks in students.items():
            avg = calculate_average(marks)
            grade = calculate_grade(avg)
            print(name, f"{avg:.2f}", grade)

# Stage 3: Find topper
    def show_topper():
        topper = ""
        highest_average = -1

        for name, marks in students.items():
            avg = calculate_average(marks)

            if avg > highest_average:
                highest_average = avg
                topper = name

        if topper:
            print("Topper:", topper)
        else:
            print("No students available.")

    print("\n===== INITIAL STUDENT RESULTS =====")
    view_all()
    show_topper()

    # Stage 4 and 5: Menu and Validation
    while True:
        print("\n===== STUDENT MARKS MANAGER =====")
        print("1. Add student")
        print("2. View all")
        print("3. Show topper")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()

            if name in students:
                print("Student already exists.")
                continue

            marks = []

            for i in range(1, 4):
                while True:
                    try:
                        mark = float(
                            input(f"Enter marks for subject {i}: ")
                        )

                        if 0 <= mark <= 100:
                            marks.append(mark)
                            break
                        else:
                            print("Invalid mark, try again.")

                    except ValueError:
                        print("Invalid mark, try again.")

            students[name] = marks
            print("Student added successfully.")

        elif choice == "2":
            view_all()

        elif choice == "3":
            show_topper()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# MAIN MENU

while True:
    print("\n========== PYTHON PROJECTS ==========")
    print("1. ATM Simulator")
    print("2. Student Marks Manager")
    print("3. Exit")

    project_choice = input("Choose a project: ")

    if project_choice == "1":
        atm_simulator()

    elif project_choice == "2":
        student_marks_manager()

    elif project_choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Choose 1, 2 or 3.")

