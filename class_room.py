import csv
import os

print("Main menu - user interaction")
print("1. Add student")
print("2. view all students")
print("3 Search Student")
print("4. Delete Student")
print("5. Exit")


price = input("Enter your choice (1, 2, 3, 4, or 5): ")

if price == "1":
    print("You selected: Add student")
#     # Add student logic here
    class addstudent:
        

        def __init__(self, name, roll_no , email, course):
            
             self.name = name
             self.roll_no = roll_no
             self.email = email
             self.course = course
             print("Student name : {self.name}, Roll No : {self.roll_no}, Email : {self.email}, Course :  {self.course}".format(self=self))
        def save(self):
            filename = "students.csv"
            file_exists = os.path.isfile(filename)
            
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Name", "Roll No", "Email", "Course"])
                writer.writerow([self.name, self.roll_no, self.email, self.course])
                
            print("Student information saved to students.csv")      
    JohnDoe = input("Enter student name: ")
    teller = input("Enter roll number: ")
    emu = input("Enter email: ")
    course = input("Enter course: ")
    my_details = addstudent(JohnDoe, teller, emu, course)
    my_details.save()

elif price == "2":
    
    print("You selected: View all students")
    class view_students:
        def view_students(self):
            filename = "students.csv"
            if os.path.isfile(filename):
                with open(filename, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        print(row)
            else:
                print("No student records found.")
    my_view = view_students()
    my_view.view_students()

elif price == "3":

    print("You selected: search students ")
    class search_student:
        def search_student(self, roll_no):
            filename = "students.csv"
            if os.path.isfile(filename):
                with open(filename, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[1] == roll_no:
                            print("Student found: {row}".format(row=row))
                            return
                    print("Student not found.")
            else:
                print("No student records found.")
    my_search = search_student()
    my_search.search_student(input("Enter roll number to search: "))
            
# elif price == "3":
    
#     print("You selected: View all students")
#     class view_students:
#         def view_students(self):
#             filename = "students.csv"
#             if os.path.isfile(filename):
#                 with open(filename, mode='r') as file:
#                     reader = csv.reader(file)
#                     for row in reader:
#                         print(row)
#             else:
#                 print("No student records found.")
#     my_view = view_students()
#     my_view.view_students()
                
# elif price == "4": 
#     print("You selected: Search Student")
#     class search_student:
#         def search_student(self, roll_no):
#             filename = "students.csv"
#             if os.path.isfile(filename):
#                 with open(filename, mode='r') as file:
#                     reader = csv.reader(file)
#                     for row in reader:
#                         if row[1] == roll_no:
#                             print("Student found: {row}".format(row=row))
#                             return
#                     print("Student not found.")
#             else:
#                 print("No student records found.")
#     my_search = search_student()
#     my_search.search_student(input("Enter roll number to search: "))
                
elif price == "4":
    print("You selected: Delete Student")
    class delete_student:
        def delete_student(self, roll_no):
            filename = "students.csv"
            if os.path.isfile(filename):
                with open(filename, mode='r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    for row in rows:
                        if row[1] != roll_no:
                            writer.writerow(row)
                print("Student with Roll No {roll_no} deleted.".format(roll_no=roll_no))
            else:
                print("No student records found.")
    my_delete = delete_student()
    my_delete.delete_student(input("Enter roll number to delete: "))
                
elif price == "5":
    print("You selected: Exit")
    exit()