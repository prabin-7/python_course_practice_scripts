def sum_of_list(lst):
    if len(lst)== 0:
        return 0
    # return sum_of_list(lst)+ lst.pop()     #this gives error(maximum recursion depth reached) as it enters infinite loop
    return lst.pop()+sum_of_list(lst) 

lst = [1,2,3,4,5,6]

print(sum_of_list(lst))

# solution by index without changing the orginal list !!!
def sum_of_list_1(lst1,index):
    if index >= len(lst1):
        return 0
    return lst1[index]+sum_of_list_1(lst1,index+1)


lst1 = [1,2,3,4,5,6]
print(sum_of_list_1(lst1,0))

