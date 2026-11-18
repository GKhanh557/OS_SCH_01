import csv
import os
import tempfile
import unittest
from helpers import DATA
import scheduler as sch
 
 
def write_temp(text):
    """Ghi text ra file tam, tra ve duong dan."""
    f = tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8")
    f.write(text)
    f.close()
    return f.name
 
 
class TestCSV(unittest.TestCase):
    def test_doc_file_hop_le(self):
        procs = sch.load_csv(os.path.join(DATA, "sample_basic.csv"))
        self.assertEqual(len(procs), 4)
        self.assertEqual(procs[0].pid, "P1")
 
    def test_header_viet_hoa_va_khoang_trang(self):
        path = write_temp(" PID , Arrival , Burst \nP1, 0 , 2\n")
        procs = sch.load_csv(path)
        self.assertEqual(procs[0].burst, 2)
        os.remove(path)
 
    def test_input_sai(self):
        cac_ca_sai = [
            "",                                          # file rong
            "pid,arrival,burst\n",                       # khong co tien trinh
            "a,b\n1,2\n",                                # sai header
            "pid,arrival,burst\nP1,0,0\n",               # burst = 0
            "pid,arrival,burst\nP1,-1,2\n",              # arrival am
            "pid,arrival,burst\nP1,x,2\n",               # khong phai so
            "pid,arrival,burst\nP1,0,1.5\n",             # so thap phan
            "pid,arrival,burst\nP1,0,1\nP1,1,1\n",       # trung pid
            "pid,arrival,burst\n,0,1\n",                 # pid rong
        ]
        for text in cac_ca_sai:
            path = write_temp(text)
            with self.assertRaises(ValueError):
                sch.load_csv(path)
            os.remove(path)
 
    def test_file_khong_ton_tai(self):
        with self.assertRaises(ValueError):
            sch.load_csv("khong_ton_tai.csv")
 
    def test_ghi_ket_qua(self):
        procs = sch.load_csv(os.path.join(DATA, "sample_basic.csv"))
        results, gantt = sch.fcfs(procs)
        folder = tempfile.mkdtemp()
        sch.save_results_csv(os.path.join(folder, "result.csv"), results)
        sch.save_trace_csv(os.path.join(folder, "trace.csv"), gantt)
 
        with open(os.path.join(folder, "result.csv"), encoding="utf-8") as f:
            rows = list(csv.reader(f))
        self.assertEqual(len(rows), 6)         # header + 4 tien trinh + dong AVG
        self.assertEqual(rows[-1][0], "AVG")
        self.assertEqual(rows[-1][6], "4.75")  # avg waiting cua FCFS
 
 
if __name__ == "__main__":
    unittest.main()
