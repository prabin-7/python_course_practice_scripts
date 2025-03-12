#Task implement a clas stack that implements the stack data structure. The class should have the following 
#methods push(x),top(),pop()
#the time complexity of each method should be O(1)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop()

    def __repr__(self):
        return str(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) # 3
print(s.top()) # 3
s.pop()
print(s.top()) # 2

print(s)    #<__main__.Stack object at 0x0000027C74B8CB60>
print(s.stack)    #[1, 2]

t1 = (10, 'apple')
t2 = (10, 'a11')

print(max(t1, t2))  