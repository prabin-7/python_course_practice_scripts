def gen_numbers(count):
    for i in range(count):
        print(i)

def print_even_numberes(count):
    list_even = []

    for i in range(count+1):
        if i %2 == 0:
            list_even.append(i)
    
    print(list_even)


#iteration over al list :
def count_even_nunbers_list(): 
    numbers=[0,1,2,3,4,5,6,7,8,9,10]
    counter=0
    for number in numbers: 
        if number%2==0:
            counter+=1
    print("Count of even no.:",counter)

count_even_nunbers_list()
gen_numbers(10)
print_even_numberes(10)

#last but not the list generate the index of the items in a list: 
def index_gen(list_1):
    list_index = []
    for item,i in enumerate(list_1):            #first one is index then second one is the item
        list_index.append((item,i))
    print(list_index)

fruits = ['orange', 'apple', 'banana', 'kiwi', 'pomogranate', 'papaya']
index_gen(fruits)
    