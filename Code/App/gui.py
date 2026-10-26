import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
 
import scheduler as sch
from gantt_view import draw_gantt, summary_line, compare_text, export_with_dialog
 
COMPARE = "So sanh ca hai"
 
 
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CPU Scheduling Simulator - FCFS & SJF")
        self.geometry("980x640")
 
        self.procs = []     # tien trinh doc tu CSV
        self.results = []   # KQ chay gan nhat
        self.gantt = []
 
        # --- Hang tren: Mo file + chon thuat toan ---
        top = ttk.Frame(self, padding=8)
        top.pack(fill="x")
        ttk.Button(top, text="Mo CSV...", command=self.open_csv).pack(side="left")
        self.path_var = tk.StringVar(value="(chua chon file)")
        ttk.Label(top, textvariable=self.path_var).pack(side="left", padx=8)
 
        self.algo = ttk.Combobox(top, state="readonly", width=22,
                                 values=list(sch.ALGORITHMS) + [COMPARE])
        self.algo.current(0)
        self.algo.pack(side="right")
        ttk.Label(top, text="Thuat toan:").pack(side="right", padx=4)
 
        # --- hang nut ---
        buttons = ttk.Frame(self, padding=(8, 0))
        buttons.pack(fill="x")
        ttk.Button(buttons, text="Chay", command=self.run).pack(side="left")
        ttk.Button(buttons, text="Xuat ket qua CSV",
                   command=self.export).pack(side="left", padx=6)
 
        # --- Bang KQ ---
        columns = ("pid", "arrival", "burst", "start", "completion",
                   "turnaround", "waiting", "response")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=9)
        for c in columns:
            self.table.heading(c, text=c)
            self.table.column(c, width=100, anchor="center")
        self.table.pack(fill="x", padx=8, pady=8)
 
        # --- Tom tat + Gantt ---
        self.summary = tk.StringVar()
        ttk.Label(self, textvariable=self.summary,
                  font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=8)
        self.canvas = tk.Canvas(self, bg="white", height=220)
        self.canvas.pack(fill="both", expand=True, padx=8, pady=8)
        self.canvas.bind("<Configure>", lambda event: draw_gantt(self.canvas, self.gantt))
 
    def open_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if path == "":
            return
        try:
            self.procs = sch.load_csv(path)
        except ValueError as e:
            messagebox.showerror("Loi du lieu", str(e))
            return
        self.path_var.set(os.path.basename(path))
        self.run()
 
    def run(self):
        if len(self.procs) == 0:
            messagebox.showinfo("Thieu du lieu", "Hay mo mot file CSV truoc")
            return
 
        name = self.algo.get()
        if name == COMPARE:
          self.summary.set(compare_text(self.procs) + "\n(Bang va Gantt: thuat toan cuoi)")
            name = list(sch.ALGORITHMS)[-1]
            self.results, self.gantt = sch.ALGORITHMS[name](self.procs)
        else:
            self.results, self.gantt = sch.ALGORITHMS[name](self.procs)
            self.summary.set(summary_line(name, self.results))
 
        # tra KQ ve bang
        self.table.delete(*self.table.get_children())
        for r in self.results:
            self.table.insert("", "end", values=(r.pid, r.arrival, r.burst, r.start,
                                                 r.completion, r.turnaround,
                                                 r.waiting, r.response))
        draw_gantt(self.canvas, self.gantt)
 
    def export(self):
        export_with_dialog(self.results, self.gantt)
 
 
if __name__ == "__main__":
    App().mainloop()
