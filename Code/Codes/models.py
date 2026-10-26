class Process:
    """Mot tien trinh doc tu file CSV."""

    def __init__(self, pid, arrival, burst, order=0):
        self.pid = pid          # tên tiến trình, ví dụ "P1"
        self.arrival = arrival  # thời điểm đến
        self.burst = burst      # thời gian cần chạy trên CPU
        self.order = order      # thứ tự trong file (dùng khi bị hòa)


class Result:
    """Ket qua cua mot tien trinh sau khi lap lich."""

    def __init__(self, pid, arrival, burst, start, completion):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.start = start                          # luc bat dau chay
        self.completion = completion                # luc chay xong
        self.turnaround = completion - arrival      # = hoan thanh - den
        self.waiting = self.turnaround - burst      # = turnaround - burst
        self.response = start - arrival             # = bat dau - den
