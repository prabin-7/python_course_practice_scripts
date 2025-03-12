def print_the_numbers(start,end):
    counter =  start
    while counter <= end:
        print(counter)
        counter += 1

def print_evem_numbers(start,end):
    counter =  start
    while counter <= end:
        if counter %2 == 0:
            print(counter)      
        counter += 1


print_evem_numbers(1,10)
print_the_numbers(1,10)