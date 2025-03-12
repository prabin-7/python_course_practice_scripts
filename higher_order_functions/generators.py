def countup(start,end):
    while start<= end:
        
        start +=1
        yield start

gen = countup(1,7)
print(gen)
for num in gen:
    print(num)