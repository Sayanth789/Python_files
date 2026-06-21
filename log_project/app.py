# import json
# import logging

# # Configure logging
# logging.basicConfig(
#     filename="attendance.log",
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s"
# )

# # Load students from JSON
# with open("student.json", "r") as file:
#     students = json.load(file)


# def find_student(student_id):
#     student_id = str(student_id)

#     if student_id in students:
#         return students[student_id]

#     logging.error(f"Student ID {student_id} not found")
#     return None


# def login(student_name):
#     logging.info(f"{student_name} logged in")
#     print(f"{student_name} logged in")


# def mark_attendance(student_name):
#     logging.info(f"{student_name} marked attendance")
#     print("Attendance marked")


# # ---- Main Program ----

# student = find_student(1)

# if student:
#     login(student)
#     mark_attendance(student)

# student = find_student(99)

import json
import logging

logging.basicConfig(
    filename="attendance.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filemode="a"   # append mode (important)
)

students = {
    "1": "Rahul",
    "2": "Anita",
    "3": "John"
}

def find_student(student_id):
    student_id = str(student_id)

    if student_id in students:
        return students[student_id]

    logging.error(f"Student ID {student_id} not found")
    return None


def login(student_name):
    logging.info(f"{student_name} logged in")
    print(f"{student_name} logged in")


def mark_attendance(student_name):
    logging.info(f"{student_name} marked attendance")
    print("Attendance marked")


student = find_student(1)

if student:
    login(student)
    mark_attendance(student)

find_student(99)
