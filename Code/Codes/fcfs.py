from metrics import build_results
 
 
def fcfs(procs):
    # Sắp xếp theo thời điểm đến; bằng nhau thì theo thứ tự trong file
    ordered = sorted(procs, key=lambda p: (p.arrival, p.order))
 
    schedule = []
    time = 0
    for p in ordered:
        start = max(time, p.arrival)   # nếu CPU rảnh thì chờ tiến trình đến
        end = start + p.burst
        schedule.append((p.pid, start, end))
        time = end
    return build_results(procs, schedule)
