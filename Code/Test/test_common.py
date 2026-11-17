import unittest
from helpers import BASIC
from Core import scheduler as sch


class TestCommon(unittest.TestCase):
    def test_gantt_lien_tuc_va_du_burst(self):
        for func in sch.ALGORITHMS.values():
            results, gantt = func(BASIC)
            for i in range(len(gantt) - 1):
                self.assertEqual(gantt[i][2], gantt[i + 1][1]) 
            total = 0
            for pid, start, end in gantt:
                if pid != "IDLE":
                    total += end - start
            self.assertEqual(total, 16)                        # 7 + 4 + 1 + 4

    def test_cong_thuc(self):
        for func in sch.ALGORITHMS.values():
            results, gantt = func(BASIC)
            for r in results:
                self.assertEqual(r.turnaround, r.completion - r.arrival)
                self.assertEqual(r.waiting, r.turnaround - r.burst)
                self.assertEqual(r.response, r.start - r.arrival)


if __name__ == "__main__":
    unittest.main()
