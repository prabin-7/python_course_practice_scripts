import time 

def some_func(name:str):
    print(f"{name} started....")
    time.sleep(5)
    print(f"{name} completed! ...")
    
def main():
    start = time.perf_counter()
    some_func("Task#1")
    print(f"Time taken: {time.perf_counter() - start}")

if __name__ == "__main__":
    main()