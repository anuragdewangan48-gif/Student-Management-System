# Student Management System

A command-line Python application to manage student records — built to 
practice Object-Oriented Programming (OOP) concepts like classes, 
inheritance, encapsulation, and polymorphism.

## 🚀 How to Run

```bash
python main.py
```

Once you run it, you'll see a menu like this:

```
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

Just type the number of the option you want and press Enter.

---

## 🧑‍🎓 How to Use Each Feature

### 1. Add Student
Select option `1` from the menu. The program will ask you to enter:
- Name
- Roll Number
- Email
- Course(s)

Once entered, a new student record is created and saved to the system.

**Example:**
```
Enter choice: 1
Enter name: John Doe
Enter roll no: 101
Enter email: john.doe@email.com
Enter course: DSAI
✅ Student added successfully!
```

---

### 2. View All Students
Select option `2` to see a list of every student currently registered, 
along with their details (name, roll number, email, course).

**Example:**
```
Enter choice: 2
101 | John Doe   | john.doe@email.com   | DSAI
102 | Jane Smith | jane.smith@email.com | CSE
```

---

### 3. Search Student
Select option `3` to find a specific student. You'll be asked to enter 
a roll number (or name), and the matching student's details will be 
displayed.

**Example:**
```
Enter choice: 3
Enter roll no to search: 101
✅ Found: John Doe | john.doe@email.com | DSAI
```

---

### 4. Update Student
Select option `4` to edit an existing student's details. Enter the 
roll number of the student you want to update, then enter the new 
information (e.g., updated email or course).

**Example:**
```
Enter choice: 4
Enter roll no to update: 101
Enter new email: anurag.new@email.com
✅ Student updated successfully!
```

---

### 5. Delete Student
Select option `5` to remove a student record. Enter the roll number 
of the student to delete, and their record will be removed from the 
system permanently.

**Example:**
```
Enter choice: 5
Enter roll no to delete: 101
✅ Student deleted successfully!
```

---

## 💾 Data Storage

All student records are saved in a `students.csv` file, so your data 
stays even after you close the program.

## 🧠 Concepts Practiced

- Classes & Objects
- Encapsulation
- Inheritance & Polymorphism
- File Handling (CSV)
