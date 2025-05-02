import threading

def print_number():
    for i in range(5):
        print(i)

thread = threading.Thread(target= print_number)
thread.start()
thread.join()