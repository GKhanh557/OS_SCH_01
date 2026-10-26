from Core.models import Process, Result
from Core.metrics import build_results, averages
from Core.fcfs import fcfs
from Core.sjf import sjf_non_preemptive
from App.csv_io import load_csv, save_results_csv, save_trace_csv

ALGORITHMS = {
    "FCFS": fcfs,
    "SJF (non-preemptive)": sjf_non_preemptive,
}
