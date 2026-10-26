from metrics import build_results
 
 
def fcfs(procs):
    # Sap xep theo thoi diem den; bang nhau thi theo thu tu trong file
    ordered = sorted(procs, key=lambda p: (p.arrival, p.order))
 
    schedule = []
    time = 0
    for p in ordered:
        start = max(time, p.arrival)   # neu CPU ranh thi cho tien trinh den
        end = start + p.burst
        schedule.append((p.pid, start, end))
        time = end
    return build_results(procs, schedule)
