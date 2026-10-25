# ==========================================
# PROJECT 1: ATM SIMULATOR
# ==========================================

correct_pin = "1234"
balance = 10000
attempts = 3
history = []

print("===== ATM SIMULATOR =====")

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Correct PIN!")
        break
    else:
        attempts = attempts - 1

        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")

if pin == correct_pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                history.append("Deposit " + str(amount))
                print("New balance:", balance)
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount > balance:
                print("Insufficient balance")
            elif amount <= 0:
                print("Invalid amount")
            else:
                balance = balance - amount
                history.append("Withdraw " + str(amount))
                print("New balance:", balance)

        elif choice == "4":
            print("Transaction History:")

            for transaction in history:
                print(transaction)

            print("Thank you!")
            break

        else:
            print("Invalid choice")

# ==========================================
# PROJECT 2: STUDENT MARKS MANAGER
# ==========================================

students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}

print("\n===== STUDENT MARKS MANAGER =====")

while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exists.")
        else:
            marks = []

            while len(marks) < 3:
                mark = float(input("Enter mark (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                else:
                    print("Invalid mark, try again.")

            students[name] = marks
            print("Student added.")

    elif choice == "2":
        for name, marks in students.items():
            average = sum(marks) / len(marks)

            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"

            print(name, round(average, 2), grade)

    elif choice == "3":
        topper = ""
        highest_average = -1

        for name, marks in students.items():
            average = sum(marks) / len(marks)

            if average > highest_average:
                highest_average = average
                topper = name

        print("Topper:", topper)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

#MENU
while True:
    print("\n========== MENU ==========")
    print("1. ATM Simulator")
    print("2. Student Marks Manager")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        print("ATM Simulator selected.")
        print("Run the ATM section above to use it.")

    elif main_choice == "2":
        print("Student Marks Manager selected.")
        print("Run the Student section above to use it.")

    elif main_choice == "3":
        print("Thank you for using the projects!")
        break

    else:
        print("Invalid choice. Please try again.")

