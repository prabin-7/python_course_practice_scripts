"""here multiprocessing.Array('i',len) is also passed py reference in python like it passes other 
mutable objects and to  print and object need to do slicing using [:]"""

import multiprocessing

def square(numbers, results):
    print(f"Process square {multiprocessing.current_process().pid} started !!")
    for idx, num in enumerate(numbers):
        results[idx] = num * num
    print(f'The results form inside the subprocess {results[:]}')  
    print(f"Process square {multiprocessing.current_process().pid} is finished!!")


def cube(numbers, results):
    print(f"Process cube {multiprocessing.current_process().pid} started !!")
    for idx, num in enumerate(numbers):
        results[idx] = num * num * num
    print(f'The results form inside the subprocess {results[:]}')
    print(f"Process cube {multiprocessing.current_process().pid} is finished!!")


def main():
    print(f"Main process started...")
    numbers = [1,2,3,4,5,6,7]
    square_result = multiprocessing.Array('i',len(numbers)) # type of data members and lenght of the created array
    cube_result = multiprocessing.Array('i',len(numbers))
    
    p1 = multiprocessing.Process(target = square, args = (numbers,square_result,)) 
    p2 = multiprocessing.Process(target = cube, args = (numbers,cube_result,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print(square_result[:])
    print(cube_result[:])
    print("Main process is finished!!")


if __name__ == "__main__":
    main()
    