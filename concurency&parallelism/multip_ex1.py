"""!!!!named the script multiprocessing which conflicted with the default 
python module and failed import at the line p = multiprocessing.Process(target = worker)
-- python tries to import from the script itself rather than the orginal python module"""

import multiprocessing
import time

def worker():
    print(f"The worker process {multiprocessing.current_process().pid} is runnning...")
    time.sleep(12)
    print("Worker is finished !!")

if __name__ == "__main__":
    p = multiprocessing.Process(target= worker)
    # print("This process is running...")
    print(f"Main process {multiprocessing.current_process().pid} is running...")
    p.start()
    
    p.join()  #wait for it at this line to finish
    time.sleep(5)
    print("Main process is finished!!")
 
    
