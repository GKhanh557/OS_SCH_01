import unittest
from helpers import BASIC, make, names
import scheduler as sch
 
 
class TestFCFS(unittest.TestCase):
    def test_basic(self):
        results, gantt = sch.fcfs(BASIC)
        # thu tu chay P1 -> P2 -> P3 -> P4
        self.assertEqual(gantt, [("P1", 0, 7), ("P2", 7, 11), ("P3", 11, 12), ("P4", 12, 16)])
        # waiting: 0, 5, 7, 7 -> trung binh 19/4 = 4.75
        self.assertEqual([r.waiting for r in results], [0, 5, 7, 7])
        self.assertEqual(sch.averages(results)["avg_waiting"], 4.75)
        # turnaround: 7, 9, 8, 11 -> trung binh 35/4 = 8.75
        self.assertEqual(sch.averages(results)["avg_turnaround"], 8.75)
 
    def test_cpu_ranh_luc_dau(self):
        results, gantt = sch.fcfs(make(("P1", 3, 2), ("P2", 4, 1)))
        self.assertEqual(gantt[0], ("IDLE", 0, 3))
 
    def test_cung_arrival_theo_thu_tu_file(self):
        results, gantt = sch.fcfs(make(("B", 0, 3), ("A", 0, 1), ("C", 0, 2)))
        self.assertEqual(names(results), ["B", "A", "C"])
 
    def test_input_khong_sap_xep(self):
        results, gantt = sch.fcfs(make(("P2", 5, 1), ("P1", 0, 2)))
        self.assertEqual(names(results), ["P1", "P2"])
 
 
if __name__ == "__main__":
    unittest.main()
