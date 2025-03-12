import functools

def cmp(a,b):
    print('compare',a,b)
    return(a-b)

numbers = [4,1,3,2] 
numbers.sort(key= functools.cmp_to_key(cmp))
print(numbers)