"""Demo of the AI-Based Student Attendance Monitoring System."""
from attendance import AttendanceManager
from attendance_analyzer import low_attendance, summary


def main():
    mgr = AttendanceManager()
    for roll, name in [(105, "Riya"), (101, "Aman"), (103, "Neha"), (102, "Karan"), (104, "Isha")]:
        mgr.add_student(roll, name)

    # Simulate 10 classes
    present_by_class = [
        [101, 102, 103, 104, 105], [101, 102, 103, 104], [101, 103, 105],
        [101, 102, 103], [101, 102, 104, 105], [101, 103],
        [101, 102, 103, 104], [101, 103, 105], [101, 102, 103], [101, 103, 104],
    ]
    for present in present_by_class:
        mgr.mark_class(present)

    print("All students (sorted by roll number):")
    for s in mgr.all_students():
        print("  ", s)

    print("\nSearch roll 103:", mgr.find_student(103))
    mgr.remove_student(104)
    print("Removed roll 104. Students left:", len(mgr.records))

    print("\nLow attendance (< 75%), lowest first:")
    for s in low_attendance(mgr):
        print("  ", s)

    print("\nSummary:", summary(mgr))


if __name__ == "__main__":
    main()
