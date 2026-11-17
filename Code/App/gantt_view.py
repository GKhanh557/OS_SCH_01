import os
from tkinter import filedialog, messagebox
 
import scheduler as sch
 
COLORS = ["#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#76b7b2",
          "#edc948", "#b07aa1", "#ff9da7", "#9c755f"]
 
 
def draw_gantt(canvas, gantt):
    """Vẽ Gantt chart lên canvas. gantt là list các bộ (pid, start, end)."""
    canvas.delete("all")
    if len(gantt) == 0:
        return
 
    width = canvas.winfo_width()
    left, top, height = 20, 50, 60
    total_time = gantt[-1][2]
    scale = (width - 2 * left) / total_time      # số pixel cho mỗi đơn vị thời gian
 
    # gán màu cho mỗi tiến trình
    pids = []
    for pid, start, end in gantt:
        if pid != "IDLE" and pid not in pids:
            pids.append(pid)
 
    canvas.create_text(left, 20, anchor="w", text="Gantt chart",
                       font=("Segoe UI", 11, "bold"))
    for pid, start, end in gantt:
        x1 = left + start * scale
        x2 = left + end * scale
        if pid == "IDLE":
            color = "#dddddd"
        else:
            color = COLORS[pids.index(pid) % len(COLORS)]
        canvas.create_rectangle(x1, top, x2, top + height, fill=color, outline="black")
        canvas.create_text((x1 + x2) / 2, top + height / 2, text=pid)
        canvas.create_text(x1, top + height + 12, text=str(start))
    canvas.create_text(left + total_time * scale, top + height + 12, text=str(total_time))
 
 
def summary_line(name, results):
    a = sch.averages(results)
    return "%s: avg WT=%.2f | avg TAT=%.2f | avg RT=%.2f" % (
        name, a["avg_waiting"], a["avg_turnaround"], a["avg_response"])
 
 
def compare_text(procs):
    """Mỗi thuật toán một dòng tóm tắt."""
    lines = []
    for name, func in sch.ALGORITHMS.items():
        results, gantt = func(procs)
        lines.append(summary_line(name, results))
    return "\n".join(lines)
 
 
def export_with_dialog(results, gantt):
    if len(results) == 0:
        messagebox.showinfo("Chưa có kết quả", "Hãy chạy thuật toán trước.")
        return
    folder = filedialog.askdirectory(title="Chọn thư mục lưu")
    if folder == "":
        return
    sch.save_results_csv(os.path.join(folder, "result.csv"), results)
    sch.save_trace_csv(os.path.join(folder, "trace.csv"), gantt)
    messagebox.showinfo("Xong", "Đã lưu result.csv và trace.csv")
    
    
     

