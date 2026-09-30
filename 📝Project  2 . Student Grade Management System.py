# 📝 Student Grade Management System

# Is project mein aap use karenge:

# Features:              | Concepts:
# 1. Student Name       | variables
# 2. Subjects           | input
# 3. Marks              | type conversion
# 4. Total Marks        | operators
# 5. Percentage         | operators
# 6. Grade              | if-elif-else
# 7. Result Display     | functions
# 8. Exit               | while loop

# ------------------------------------------
# Student Data
# ------------------------------------------


student_subjects = []
student_marks = []

# ------------------------------------------
# Student Information Function
# ------------------------------------------
def student_information():
    student_name = input("enter the students name:")
    return student_name

         


# ------------------------------------------
# Marks Function
# ------------------------------------------

def marks():
    global student_subjects
    global student_marks

    student_subjects = []
    student_marks = []

    for i in range(5):

        subject = input("Enter the subject name: ")
        student_subjects.append(subject)

        mark = float(input(f"Enter the marks for subject {subject}: "))
        student_marks.append(mark)

    print("Marks entered successfully")


# ------------------------------------------
# Result Function
# ------------------------------------------

def result():
    total_marks = sum(student_marks)
    percentage = (total_marks / 500) * 100

    print("Your total marks are:", total_marks)
    print("Your percentage is:", percentage, "%")

# ------------------------------------------
# Grade Function
# ------------------------------------------


def grade():
    total_marks = sum(student_marks)
    percentage = (total_marks / 500) * 100

    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"


# ------------------------------------------
# Main Menu
# ------------------------------------------
while True:

    print("\n----- STUDENT GRADE MANAGEMENT SYSTEM -----")
    print("1. Student Information")
    print("2. Enter Marks")
    print("3. Show Result")
    print("4. Show Grade")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = student_information()
        print("Student name is:", student_name)

    elif choice == "2": 
        marks()

    elif choice == "3":
        result()

    elif choice == "4":
        student_grade = grade()
        print("Your grade is:", student_grade)

    elif choice == "5":
        print("Thank you for using Student Grade Management System")
        break

    else:
        print("Invalid choice. Please try again")