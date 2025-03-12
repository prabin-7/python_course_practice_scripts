class CountUp:
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current
#create an iterator    
counter = CountUp(1,10)

#itierate throug the iterator 
for num in counter:
    print(num)
