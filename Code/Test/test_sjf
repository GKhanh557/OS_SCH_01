import unittest
from helpers import BASIC, make, names
import scheduler as sch
 
 
class TestSJF(unittest.TestCase):
    def test_basic(self):
        results, gantt = sch.sjf_non_preemptive(BASIC)
        # P1 chạy 0-7. Lúc 7 có P2(4), P3(1), P4(4) -> chọn P3.
        # Sau đó P2 và P4 cùng burst 4, P2 đến sớm hơn nên P2 trước.
        self.assertEqual(gantt, [("P1", 0, 7), ("P3", 7, 8), ("P2", 8, 12), ("P4", 12, 16)])
        # waiting: P1=0, P3=3, P2=6, P4=7 -> trung bình 16/4 = 4.0
        self.assertEqual(sch.averages(results)["avg_waiting"], 4.0)
        # turnaround: 7, 4, 10, 11 -> trung bình 32/4 = 8.0
        self.assertEqual(sch.averages(results)["avg_turnaround"], 8.0)
 
    def test_cpu_ranh_luc_dau(self):
        results, gantt = sch.sjf_non_preemptive(make(("P1", 3, 2), ("P2", 4, 1)))
        self.assertEqual(gantt[0], ("IDLE", 0, 3))
 
    def test_mot_tien_trinh(self):
        results, gantt = sch.sjf_non_preemptive(make(("P1", 0, 5)))
        self.assertEqual(gantt, [("P1", 0, 5)])
 
    def test_hoa_het_theo_thu_tu_file(self):
        results, gantt = sch.sjf_non_preemptive(make(("B", 0, 3), ("A", 0, 3), ("C", 0, 3)))
        self.assertEqual(names(results), ["B", "A", "C"])
 
    def test_hoa_burst_thi_arrival_som_hon_truoc(self):
        results, gantt = sch.sjf_non_preemptive(make(("P1", 0, 5), ("P3", 3, 2), ("P2", 1, 2)))
        self.assertEqual(names(results), ["P1", "P2", "P3"])
 
    def test_khong_bi_ngat(self):
        # P2 ngắn hơn nhưng đến khi P1 đang chạy -> P1 vẫn chạy hết
        results, gantt = sch.sjf_non_preemptive(make(("P1", 0, 10), ("P2", 1, 1)))
        self.assertEqual(gantt, [("P1", 0, 10), ("P2", 10, 11)])
 
    def test_sjf_wait_khong_te_hon_fcfs(self):
        fcfs_wait = sch.averages(sch.fcfs(BASIC)[0])["avg_waiting"]
        sjf_wait = sch.averages(sch.sjf_non_preemptive(BASIC)[0])["avg_waiting"]
        self.assertTrue(sjf_wait <= fcfs_wait)
 
 
if __name__ == "__main__":
    unittest.main()
