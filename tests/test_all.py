
import os, sys, unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from data_structures import BST, PriorityQueue
from attendance import AttendanceManager
from attendance_analyzer import low_attendance


class TestBST(unittest.TestCase):
    def setUp(self):
        self.t = BST()
        for k in [50, 30, 70, 20, 40, 60, 80]:
            self.t.insert(k, str(k))

    def test_search(self):
        self.assertEqual(self.t.search(60), "60")
        self.assertIsNone(self.t.search(99))

    def test_inorder_sorted(self):
        self.assertEqual(self.t.inorder(), ["20", "30", "40", "50", "60", "70", "80"])

    def test_delete_leaf_one_child_two_children(self):
        self.assertTrue(self.t.delete(20))
        self.assertTrue(self.t.delete(30))
        self.assertTrue(self.t.delete(50))
        self.assertFalse(self.t.delete(999))
        self.assertEqual(self.t.inorder(), ["40", "60", "70", "80"])
        self.assertEqual(len(self.t), 4)


class TestPQ(unittest.TestCase):
    def test_order(self):
        pq = PriorityQueue()
        for p in [5, 1, 4, 2, 3]:
            pq.push(p, p)
        self.assertEqual([pq.pop()[0] for _ in range(5)], [1, 2, 3, 4, 5])
        with self.assertRaises(IndexError):
            pq.pop()


class TestAttendance(unittest.TestCase):
    def test_flow(self):
        m = AttendanceManager()
        m.add_student(1, "A")
        m.add_student(2, "B")
        for present in ([1, 2], [1], [1], [1]):
            m.mark_class(present)
        self.assertEqual(m.find_student(1).percentage, 100.0)
        self.assertEqual(m.find_student(2).percentage, 25.0)
        self.assertEqual([s.roll_no for s in low_attendance(m)], [2])
        with self.assertRaises(ValueError):
            m.add_student(1, "dup")


if __name__ == "__main__":
    unittest.main()
  
