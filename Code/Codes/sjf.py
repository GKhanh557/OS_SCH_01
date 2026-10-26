from metrics import build_results
 
 
def sjf_non_preemptive(procs):
    remaining = list(procs)   # các tiến trình chưa chạy
    schedule = []
    time = 0
 
    while len(remaining) > 0:
        # 1. Lấy các tiến trình đã đến
        ready = []
        for p in remaining:
            if p.arrival <= time:
                ready.append(p)
 
        # 2. Chưa ai đến: CPU rảnh, nhảy đến lúc tiến trình sớm nhất đến
        if len(ready) == 0:
            time = min(p.arrival for p in remaining)
            continue
 
        # 3. Chọn burst nhỏ nhất. Hòa thì xét arrival, rồi thứ tự trong file
        chosen = min(ready, key=lambda p: (p.burst, p.arrival, p.order))
 
        # 4. Cho chạy đến hết (không bị ngắt)
        schedule.append((chosen.pid, time, time + chosen.burst))
        time = time + chosen.burst
        remaining.remove(chosen)
 
    return build_results(procs, schedule)
