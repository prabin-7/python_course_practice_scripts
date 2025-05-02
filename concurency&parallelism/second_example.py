import threading


print_lock = threading.Lock()  #creating a lock to prevent printing() on same line as print() is not thread safe by default
def task(name:str):
    with print_lock:
        print(f"Task {name} started ....")
    for i in range(5):
        with print_lock:
            print(f"Task {name} printing {i+1}") #i+1 so it starts counting from 1  \n adds newline but print() has newline by default
    with print_lock:
        print(f"Task {name} finished!")


def main():
    
    threads = [threading.Thread(target= task, args = (f"Thread#{i}",)) for i in range(1,4)]
    # task('A')
    # task('B')
    for t in threads:
        t.start()
        
    # for t in threads:
    #     t.join()
 ''' commenting the t.join() for each thread prevents the waiting for the thread to complete before 
 completeing the main thread'''       
        
if __name__ == '__main__':
    print("main thread started")
    main()
    print("main thread end!!")