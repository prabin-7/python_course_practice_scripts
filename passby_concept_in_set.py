'''to check if when a list is made into a set the orginal set changes or not'''

list=[1,2,3,4,5,6,7,6,5,4,3,2,1]
set_list = set(list)
set(list)
print(set_list)
print(list)  
'''bhanesi tyo function ma pass bhayera tesma aru kei operation bhaye paxi matra change hunxa'''
def fxn_change_list(a:list)->list:
    # a = a.append((1,2))     #the function append modifies the orginal list and returns None
    a.append(1)                #use this for desired results
    return a 
print(fxn_change_list(list))
print(list)