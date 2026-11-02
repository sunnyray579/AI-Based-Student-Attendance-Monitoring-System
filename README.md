# AI-Based Student Attendance Monitoring System

Data Structures and Algorithms – II (CCSE0301) · PBL Project · SDG 4 – Quality Education

A Python project that organises student records, tracks attendance, calculates
attendance percentages and flags students with low attendance.

## Data structures used
| Concept | Where | Purpose |
|---|---|---|
| Binary Search Tree | `data_structures.py` → `BST` | Store student records keyed by roll number; insert, search, delete |
| Priority Queue (min-heap) | `data_structures.py` → `PriorityQueue` | Serve the lowest-attendance students first |

## Project structure
```
main.py                  # demo / program entry point
student.py               # Student record
attendance.py            # attendance marking + record management
attendance_analyzer.py   # percentages and low-attendance detection
data_structures.py       # BST and Priority Queue
tests/test_all.py        # unit tests
```

## Run
```bash
python main.py                      # run the demo
python -m unittest discover tests   # run the tests
```
Requires Python 3.8+ (no external packages).

## Future improvements
Face-recognition attendance, real-time dashboard, SMS/email alerts for low
attendance, database storage, report generation and a user interface.

## Author
Sunny Kumar Ray
