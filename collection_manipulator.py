Students = []

while True:
    print("\nWelcome to the Student Data Organizer!")

    print("Select an option:")
    print("1. Add student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subject Offered")
    print("6. Exit")

    choice=int(input("Enter your choice: "))

    match choice:
        case 1:

            print("\nEnter student details")
            stud_id=int(input("Student ID: "))
            Name=input("Name: ")
            Age=int(input("Age: "))
            Grade=input("Grade: ")
            DOB=input("Date of Birth (YYYY-MM-DD): ")
            Subjects=input("Subjects(comma-separated): ")

            student= {
                "id":stud_id,
                "name":Name,
                "age":Age,
                "grade":Grade,
                "dob":DOB,
                "subject": Subjects
            }

            Students.append(student)

            print("\n Student added successfully!")

        case 2:
            print("\n --- Display All Students ---")

            if len(Students)==0:
                print("No students found.")

            else:
                for student in Students:
                    print(
                        f"Student ID: {student['id']} | "
                        f"Name: {student['name']} | "
                        f"Age: {student['age']} | "
                        f"Grade: {student['grade']} | "
                        f"Subjects: {student['subject']} | "
                    )

        case 3:
            student_id = int(input("Enter Student id to update: "))

            found = False

            for student in Students:
                if student["id"] == student_id:
                    student["name"] = input("Enter new name: ")
                    student["age"] = int(input("Enter new age: "))
                    student["grade"] = input("Enter new grade: ")
                    student["dob"] = input("Enter new Date of Birth: ")
                    student["subject"] = input("Enter new subjects: ")

                    print("Student Information Updated Successfully!")

                    found = True
                    break

            if found == False:
                print("Student not found.")

        case 4:

            student_id=int(input("Enter Student id to delete:"))

            found=False

            for student in Students:
                if student["id"]==student_id:
                    Students.remove(student)

                    print("Student Delete Successfully!")

                    found=True
                    break

                if found==False:
                    print("Student not found.")

        case 5:
            print("\n --- Subject Offered ---")

            print("Math")
            print("science")
            print("English")

        case 6:
            print("\n Thank You!!")
            break


        case _:
            print("\nInvalid Choice !")










