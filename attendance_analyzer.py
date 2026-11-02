"""Attendance percentages and low-attendance detection (Priority Queue)."""
from data_structures import PriorityQueue


def low_attendance(manager, threshold=75.0):
    """Return students below threshold%, lowest attendance first."""
    pq = PriorityQueue()
    for s in manager.all_students():
        if s.total_classes > 0 and s.percentage < threshold:
            pq.push(s.percentage, s)
    result = []
    while not pq.is_empty():
        result.append(pq.pop()[1])
    return result


def summary(manager):
    students = manager.all_students()
    if not students:
        return {"students": 0, "average": 0.0}
    avg = sum(s.percentage for s in students) / len(students)
    return {"students": len(students), "average": round(avg, 2)}
