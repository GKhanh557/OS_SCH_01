# OS_SCH_01

## 👥 Thanh vien nhom

| STT | Ho Và Ten | MSSV | Tai Khoan github | Vai Tro | Phan Cong |
|---|---|---|---|---|
| 1 | Nguyen Duong Gia Khanh | 056307008420 | @Gkhanh557 | Truong nhom | Data model, tính metrics, ghép module, Test tổng hợp |
| 2 | Vo Dinh Bao | 062207006568 | @baokt2307-beep | Thanh Vien | Thuật toán SJF non-preemptive, test SJF |
| 3 | Nguyen Huu Quoc Huy | 056207008300 | @username_huy | Thanh Vien | Thuật toán FCFS, test FCFS |
| 4 | Tran Nhat Hao | 054207005647 | @haotn545647-rgb | Thanh Vien | Gantt chart, so sánh, xuất CSV, hiệu năng |
| 5 | Le Hoang Viet | 064207010735 | VietLH0103 | Thanh Vien | Đọc/ghi CSV, cửa sổ chính, test CSV, input sai |

# CPU Scheduling Simulator: FCFS & SJF (OS_SCH_01)

Ứng dụng desktop (Python + Tkinter) mô phỏng FCFS và SJF non-preemptive:
đọc CSV, tính waiting/turnaround/response time, vẽ Gantt chart, xuất kết quả CSV.

## Yêu cầu
- Python 3.9+ (Tkinter có sẵn trên Windows). Không cần cài thêm thư viện.

## Chạy
```
python gui.py
```
Bấm **Mở CSV...** (thử `data/sample_basic.csv`), chọn thuật toán, bấm **Chạy**.
Bấm **Xuất kết quả CSV** để lưu `result.csv` và `trace.csv` (Gantt).

## Định dạng input
```
pid,arrival,burst
P1,0,7
```
`arrival` >= 0, `burst` > 0 (số nguyên), `pid` không rỗng và không trùng.

## Quy ước thuật toán
- Thời gian: CPU rảnh mà chưa có tiến trình đến thì ghi `IDLE`.
- FCFS: theo arrival, bằng nhau thì theo thứ tự trong file.
- SJF non-preemptive: khi CPU rảnh chọn tiến trình đã đến có burst ngắn nhất;
  tie-break: burst -> arrival -> thứ tự trong file.
- Turnaround = completion - arrival; Waiting = turnaround - burst; Response = start - arrival.

## Kiểm thử
```
python -m unittest discover tests     # test đúng/biên/tie/input lỗi, oracle tính tay
python tests/perf_test.py             # hiệu năng n = 100 .. 5000
```

`data/` chứa CSV mẫu (basic, idle, tie, bad_burst để thử xử lý lỗi).
