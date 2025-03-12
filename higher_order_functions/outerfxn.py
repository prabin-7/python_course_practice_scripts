def outer(message):
    def inner():
        print(message)
    return inner


hello = outer("hello from the other side i must have called you thousand times to tellyou i am sorry for everthing that you've done" )

hello()


def apply_add(func,x,y):
    return func(x,y)

def add(a,b):
    return a+b

results = apply_add(add, 109,201)
print(results)