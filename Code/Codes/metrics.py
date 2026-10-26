from Core.models import Result


def build_results(procs, schedule):
    """schedule la list cac bo (pid, start, end) theo thu tu CPU chay.
    Tra ve (results, gantt). Gantt co them doan "IDLE" khi CPU ranh."""
    results = []
    gantt = []
    time = 0
    for pid, start, end in schedule:
        if start > time:                      # CPU ranh tu time den start
            gantt.append(("IDLE", time, start))
        gantt.append((pid, start, end))
        time = end

        for p in procs:                       # tim tien trinh tuong ung
            if p.pid == pid:
                results.append(Result(p.pid, p.arrival, p.burst, start, end))
    return results, gantt


def averages(results):
    """Tinh trung binh waiting, turnaround, response."""
    n = len(results)
    total_wait = 0
    total_turn = 0
    total_resp = 0
    for r in results:
        total_wait += r.waiting
        total_turn += r.turnaround
        total_resp += r.response
    return {
        "avg_waiting": total_wait / n,
        "avg_turnaround": total_turn / n,
        "avg_response": total_resp / n,
    }
