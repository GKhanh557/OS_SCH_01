import random
import time
from helpers import make
import scheduleer as sch

random.seed(42) 
print("%8s %12 %12" % ("n", "FCFS (giay)","SJF (giay)"))

for n in (100, 500 , 1000, 3000, 5000):
  rows=[]
  for i in range(n):
    rows.append(("P" + str(i), ramdom.randint(0, n), ramdom.randint(1, 20)))
  procs = make(*rows)

t = time.perf_counter()
sch.fcfs(procs)
t_fcfs = time.perf_counter() - t

t = time.perf_counter()
sch.sjf_non_preemptive(procs)
t_sjf = time.perf_counter() - t

print("%8d %12.4f %12.4f" % (n, t_fcfs, t_sjf))
    
    
     

