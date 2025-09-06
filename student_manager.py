"""
Student Management System - CRUD Application
Week 2 Python Project
Features: Create, Read, Update, Delete student records
"""

import json
import os
from datetime import datetime

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    
    def load_students(self):
        """Load students from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file: # 'r' open for reading (default)
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def save_students(self):
        """Save student to JSON file"""
        with open(self.filename, 'w') as file:  # 'w' open for writing, truncating the file first
            json.dump(self.students, file, indent=4)

    def create_student(self):
        """Create a student"""
        print("\n--- Create New Student ---")
        try:
            student_id = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            course = input("Enter Course: ").strip()
            email = input("Enter Email: ").strip()

            # Check if student ID already exists
            for student in self.students:
                if student['student_id'] == student_id:
                    print("Error: Student ID already exists!")
                    return
                
            new_student = {
                'student_id': student_id,
                'name': name,
                'age': age,
                'course': course,
                'email': email,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            self.students.append(new_student)
            self.save_students()
            print("Student created successfully!")
        except ValueError:
            print("Error: Age must be a number!")
        except Exception as e:
            print(f"Error creating student: {e}")

    def read_students(self):
        """Read and display all students"""
        print("\n--- All Students ---")

        if not self.students:
            print("No students found.")
            return
        
        for i, student in enumerate(self.students, 1):
            print(f"\n{i}. ID: {student['student_id']}")
            print(f"    Name: {student['name']}")
            print(f"    Age: {student['age']}")
            print(f"    Course: {student['course']}")
            print(f"    Email: {student['email']}")
            print(f"    Created: {student['created_at']}")
            print(f"    Updated: {student['updated_at']}")

    
    def update_student(self):
        """Update an existing student record"""
        print("\n--- Update Student ---")

        student_id = input("Enter Student ID to update: ").strip()

        for student in self.students:
            if student['student_id'] == student_id:
                print(f"Updating student: {student['name']}")

                try:
                    name = input(f"Enter new name ({student['name']}): ").strip()
                    age = input(f"Enter new age ({student['age']}): ").strip()
                    course = input(f"Enter new course ({student['course']}): ").strip()
                    email = input(f"Enter new email ({student['email']}): ").strip()

                    if name:
                        student['name'] = name
                    if age:
                        student['age'] = int(age)
                    if course:
                        student['course'] = course
                    if email:
                        student['email'] = email

                    student['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_students()
                    print("Student updated successfully!")
                    return

                except ValueError:
                    print("Error: Age must be a number!")
                    return
        
        print("Error: student not found!")

    
    def delete_student(self):
        """Delete a student"""
        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID to delete: ").strip()

        for i, student in enumerate(self.students):
            if student['student_id'] == student_id:
                confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").lower()

                if confirm == 'y':
                    del self.students[i]
                    self.save_students()
                    print("Student deleted successfully!")
                    return
                else:
                    print("Deletion cancelled.")
                    return
                
        print("Error: Student not found!")

    def search_student(self):
        """Search a student"""
        print("\n--- Search Student ---")

        search_term = input("Enter Student ID or Name to search: ").strip().lower()

        found_students = []
        for student in self.students:
            if (search_term in student['student_id'].lower() or search_term in student['name'].lower()):
                found_students.append(student)

            if found_students:
                print(f"\nFound {len(found_students)} student(s):")
                for i, student in enumerate(found_students, 1):
                    print(f"\n{i}. ID: {student['student_id']}")
                    print(f"    Name: {student['name']}")
                    print(f"    Age: {student['age']}")
                    print(f"    Course: {student['course']}")
                    print(f"    Email: {student['email']}")
            else:
                print("No students found matching your search.")

    
    def display_statistics(self):
        """Display basic statistics"""
        print("\n--- Statistics ---")
        print(f"Total Students: {len(self.students)}")
        
        if self.students:
            courses = {}
            ages = [student['age'] for student in self.students]
            
            for student in self.students:
                course = student['course']
                # print(f"course: {course}")
                courses[course] = courses.get(course, 0) + 1
            
            # print(f"Courses: {courses}") # return ==> Courses: {'Python Programming': 1, 'Java Programming': 1}

            # Average calculation: sum(ages) adds all ages, divides by number of students
            # Formatting: :.1f formats the result to 1 decimal place
            print(f"Average Age: {sum(ages) / len(ages):.1f}")
            print("Students by Course:")
            for course, count in courses.items():
                print(f"  {course}: {count} student(s)")

def main(): 
    """Main function to run the Student Management Systems"""
    manager = StudentManager()

    while True:
        print("\n" + "="*50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1.   Create Student")
        print("2.   View All Students")
        print("3.   Update Student")
        print("4.   Delete Student")
        print("5.   Search Student")
        print("6.   Statistics")
        print("7.   Exit")
        print("="*50)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            manager.create_student()
        elif choice == '2':
            manager.read_students()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            manager.search_student()
        elif choice == '6':
            manager.display_statistics()
        elif choice == '7':
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
