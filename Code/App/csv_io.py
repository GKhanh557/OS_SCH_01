import csv
from models import Process
from metrics import averages
 
 
def load_csv(path):
    """Doc file co header: pid,arrival,burst. Du lieu sai thi in ra ValueError."""
    try:
        f = open(path, newline="", encoding="utf-8-sig")
    except OSError:
        raise ValueError("Khong mo duoc file: " + path)
 
    procs = []
    used_pids = []
    with f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("File rong")
        headers = [h.strip().lower() for h in reader.fieldnames]
        for need in ("pid", "arrival", "burst"):
            if need not in headers:
                raise ValueError("Thieu cot '" + need + "' trong header")
 
        line = 1
        for row in reader:
            line += 1
            # Chuan hoa ten cot va khoang trong thua
            data = {}
            for key, value in row.items():
                data[key.strip().lower()] = (value or "").strip()
 
            pid = data["pid"]
            if pid == "":
                raise ValueError("Dong " + str(line) + ": pid rong")
            if pid in used_pids:
                raise ValueError("Dong " + str(line) + ": pid bi trung")
            try:
                arrival = int(data["arrival"])
                burst = int(data["burst"])
            except ValueError:
                raise ValueError("Dong " + str(line) + ": arrival/burst phai la so nguyen")
            if arrival < 0:
                raise ValueError("Dong " + str(line) + ": arrival khong duoc am")
            if burst <= 0:
                raise ValueError("Dong " + str(line) + ": burst phai lon hon 0")
 
            used_pids.append(pid)
            procs.append(Process(pid, arrival, burst, len(procs)))
 
    if len(procs) == 0:
        raise ValueError("File khong co tien trinh nao")
    return procs
 
 
def save_results_csv(path, results):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pid", "arrival", "burst", "start", "completion",
                    "turnaround", "waiting", "response"])
        for r in results:
            w.writerow([r.pid, r.arrival, r.burst, r.start, r.completion,
                        r.turnaround, r.waiting, r.response])
        a = averages(results)
        w.writerow(["AVG", "", "", "", "",
                    round(a["avg_turnaround"], 2),
                    round(a["avg_waiting"], 2),
                    round(a["avg_response"], 2)])
 
 
def save_trace_csv(path, gantt):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["pid", "start", "end"])
        for pid, start, end in gantt:
            w.writerow([pid, start, end])
