"""Attendance marking and record management (backed by a BST)."""
from data_structures import BST
from student import Student


class AttendanceManager:
    def __init__(self):
        self.records = BST()

    def add_student(self, roll_no, name):
        if self.records.search(roll_no) is not None:
            raise ValueError(f"Roll number {roll_no} already exists")
        self.records.insert(roll_no, Student(roll_no, name))

    def remove_student(self, roll_no):
        return self.records.delete(roll_no)

    def find_student(self, roll_no):
        return self.records.search(roll_no)

    def mark_attendance(self, roll_no, present):
        """Record one class for a student: present=True/False."""
        student = self.find_student(roll_no)
        if student is None:
            raise KeyError(f"Roll number {roll_no} not found")
        student.total_classes += 1
        if present:
            student.attended += 1

    def mark_class(self, present_roll_numbers):
        """Mark one class for everyone: listed roll numbers are present."""
        present = set(present_roll_numbers)
        for s in self.records.inorder():
            self.mark_attendance(s.roll_no, s.roll_no in present)

    def all_students(self):
        return self.records.inorder()
