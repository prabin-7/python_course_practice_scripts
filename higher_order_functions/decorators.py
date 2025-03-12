def printer(func):
    def wrapper(*args,**kwargs):
        print(f'the function name before calling {func.__name__}')
        func(*args,**kwargs)
        print(f'the function name after calling{func.__name__}')
    return wrapper

@printer
def hello(name:str):
    print(f'hello {name}')

hello('prabin')