import json
import os

class Student:
    """This class represents a student"""

    def __init__(self, name, course, email, hallticket, gender):
        self.name = name
        self.course = course
        self.email = email
        self.hallticket = hallticket
        self.gender = gender

    def __repr__(self):
        return f"name = {self.name}, email = {self.email}, course = {self.course}, hallticket = {self.hallticket}, gender = {self.gender}"

    def to_dict(self):
        return {
            "name": self.name,
            "course": self.course,
            "email": self.email,
            "hallticket": self.hallticket,
            "gender": self.gender
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data.get("name", ""),
            data.get("course", ""),
            data.get("email", ""),
            data.get("hallticket", "N/A"),  # default if missing
            data.get("gender", "N/A")       # default if missing
           )


# File for saving data
DATA_FILE = "students.json"


# Load existing students if file exists
def load_students():
    abs_path = os.path.abspath(DATA_FILE)
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            print(f"📂 Loaded {len(data)} students from: {abs_path}")
            return {email: Student.from_dict(st) for email, st in data.items()}
    else:
        print(f"📂 No existing data file found. A new one will be created at: {abs_path}")
    return {}


# Save students to file
def save_students():
    abs_path = os.path.abspath(DATA_FILE)
    with open(DATA_FILE, "w") as f:
        data = {email: st.to_dict() for email, st in student_dict.items()}
        json.dump(data, f, indent=4)
    print(f"💾 Data saved to: {abs_path}")


# Global storage (in-memory)
student_dict = load_students()


def add_student():
    """This function adds the student info"""
    name = input("Enter student's name: ").strip()
    if not name.replace(" ", "").isalpha():
        print("❌ Name must contain only letters and spaces.")
        return

    course = input("Enter course: ").strip()
    if not course:
        print("❌ Course cannot be empty.")
        return

    email = input("Enter email id: ").strip().lower()
    if "@" not in email or "." not in email:
        print("❌ Invalid email format.")
        return
    
    hallticket = input("Enter hallticket number: ").strip()
    if not hallticket.isalnum():
        print("❌ Hallticket must contain only letters/numbers.")
        return
    
    gender = input("Enter Gender (Male/Female/Other): ").strip()
    if not gender.isalpha():
        print("❌ Gender must contain only letters.")
        return

    if email in student_dict:
        overwrite = input(
            "⚠️ This email already exists. Overwrite? (y/n): "
        ).strip().lower()
        if overwrite != "y":
            print("Student not updated.")
            return

    student = Student(name, course, email, hallticket, gender)
    student_dict[email] = student
    save_students()
    print("✅ Student added/updated successfully.")


def fetch_student_details():
    """This function fetches the student details"""
    email = input("Enter the email id of the student: ").strip().lower()
    if email in student_dict:
        student = student_dict[email]
        print("----- Student Details -----")
        print(f"Name      : {student.name}")
        print(f"Email     : {student.email}")
        print(f"Course    : {student.course}")
        print(f"Hallticket: {student.hallticket}")
        print(f"Gender    : {student.gender}")
        print("---------------------------")
    else:
        print("❌ Student not found.")


def list_all_students():
    """This function lists all students"""
    if not student_dict:
        print("⚠️ No students found in the system.")
        return

    print("\n📋 All Students:")
    print("-" * 60)
    for i, student in enumerate(student_dict.values(), start=1):
        print(f"{i}. {student.name} | {student.course} | {student.email} | {student.hallticket} | {student.gender}")
    print("-" * 60)


def delete_student():
    """This function deletes a student by email"""
    email = input("Enter the email id of the student to delete: ").strip().lower()
    if email in student_dict:
        confirm = input(f"⚠️ Are you sure you want to delete {student_dict[email].name}? (y/n): ").strip().lower()
        if confirm == "y":
            del student_dict[email]
            save_students()
            print("🗑️ Student deleted successfully.")
        else:
            print("❌ Deletion cancelled.")
    else:
        print("❌ Student not found.")


def menu():
    """This is menu for the application"""
    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add or update student")
        print("2. Fetch student info by email")
        print("3. Exit")
        print("4. List all students")
        print("5. Delete a student")
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            fetch_student_details()
        elif choice == "3":
            break
        elif choice == "4":
            list_all_students()
        elif choice == "5":
            delete_student()
        else:
            print("⚠️ Invalid choice, please enter 1, 2, 3, 4, or 5.")
    print("👋 Thanks for using the Student Management System!")


if __name__ == "__main__":
    menu()
