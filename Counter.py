#   @author: Mikolaj Roszczyk, 
#   @company: Intel
#
#   INTEL DEVELOPER CLOUD Demo Code

import time
from threading import Thread
import platform
from multiprocessing import Pool

COUNT_MAX=10000000
THREADS=15

def task(task_id):
    begin=time.time()
    i=0
    condition=False

    while not condition:
        i=i+1
        if(i==COUNT_MAX):
            condition=True
        
    print(f"Thread {task_id} counted to {i} in {time.time()-begin}")
    
if __name__ == "__main__":
    num_processes = 8 

    begin=time.time()
    with Pool(processes=num_processes) as pool:
        pool.map(task, range(num_processes))
    print(f"Time spent on all threads: {time.time()-begin}")