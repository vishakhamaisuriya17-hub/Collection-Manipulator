# Collection Manipulator

Student Data Organizer is a Python console-based application designed to manage student information efficiently. The program provides a simple menu-driven interface that allows users to add, display, update, and delete student records. It also displays the subjects offered by the organization.

This project demonstrates the use of Python lists, dictionaries, loops, conditional statements, user input, and the `match-case` statement.

---

## Features

- Add new student information.
- Display all student records.
- Update existing student information.
- Delete a student record using the Student ID.
- Display the subjects offered.
- Menu-driven interface.
- Continuous program execution until the user chooses to exit.

---

## Technologies Used

- Python 3.x
- Visual Studio Code

---

## Concepts Covered

- Lists
- Dictionaries
- `while` Loop
- `for` Loop
- `if-else` Statements
- `match-case`
- User Input
- Dictionary Keys and Values
- List Methods
- Searching Records
- Updating Records
- Deleting Records

---

## Student Information Stored

The program stores the following information for each student:

- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

---

## Project Structure

```text
PR_3/
│
├── collection_manipulator.py
└── README.md
```

---

## Menu Options

The application provides the following options:

```text
1. Add student
2. Display All Student
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/vishakhamaisuriya17-hub/Collection-Manipulator.git
```

### 2. Navigate to the Project Folder

```bash
cd PR_3
```

### 3. Run the Python Program

```bash
python Collection_Manipulator.py
```

---

## Sample Output

### Main Menu

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add student
2. Display All Student
3. Update Student Information
4. Delete Student
5. Display Subject Offered
6. Exit

Enter your choice:
```

### Add Student

```text
Enter student details

Student ID: 101
Name: Alice
Age: 20
Grade: A
Date of Birth (YYYY-MM-DD): 2005-05-10
Subjects(comma-separated): Math, Science, English

Student added successfully!
```

### Display Students

```text
Student ID: 101 | Name: Alice | Age: 20 | Grade: A | Subjects: Math, Science, English
```

### Update Student

The user can enter a Student ID and update the following information:

- Name
- Age
- Grade
- Date of Birth
- Subjects

### Delete Student

The user can delete a student record by entering the Student ID.

---

## Subjects Offered

The program currently displays the following subjects:

```text
Math
Science
English
```

---

## Learning Outcomes

This project helps beginners understand:

- How to store multiple records using a list of dictionaries.
- How to add new data to a list.
- How to search for a specific record using an ID.
- How to update dictionary values.
- How to delete records from a list.
- How to use loops for data processing.
- How to create a menu-driven Python application.
- How to use Python's `match-case` statement.

---

## Future Enhancements

- Add student search functionality.
- Add student sorting by name, age, or grade.
- Add input validation.
- Prevent duplicate Student IDs.
- Store data permanently using a file or database.
- Add more subjects.
- Add student attendance management.
- Add marks and result management.
- Add a graphical user interface.

---

## Author

**Vishakha Jayeshbhai Maisuriya**

---

## License

This project is created for learning and educational purposes.
