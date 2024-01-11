#   @author: Mikolaj Roszczyk, 
#   @company: Intel
#
#   INTEL DEVELOPER CLOUD Demo Code

import time
from threading import Thread
import platform
# from concurrent import futures
from metaflow import Parameter

COUNT_MAX=10000000
THREADS=15

def task():
    begin=time.time()
    i=0
    condition=False

    while not condition:
        i=i+1
        if(i==COUNT_MAX):
            condition=True
        
    print(f"Thread counted to {i} in {time.time()-begin}")

def imhere(i):
    for x in range(10):
        print(f"{x} I'm here: {i}")

threads=[]

begin=time.time()

num_cores=Parameter('num-cores')
print(num_cores)

for i in range(THREADS):
    # threads.append(Thread(target=imhere, args=[i]))
    threads.append(Thread(target=task))

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()
    
print(f"{THREADS} threads counted to {COUNT_MAX} in {time.time()-begin}")
print("processor: ", platform.processor()) #https://en.wikichip.org/wiki/intel/cpuid


# Additional SOURCES:
# https://outerbounds.com/docs/use-multiple-cpu-cores/