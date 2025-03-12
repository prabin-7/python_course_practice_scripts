def countdown(a):
    if a <= 0:
        print('blast off')
    
    else:
        print(a)
        countdown(a-1)

    


def factorial(n,f=1):
    if n == 1: 
        print('the factorial is:',f)

    else: 
        f *= n
        n -= 1
        factorial(n,f)


countdown(5)
factorial(2)

 

# print(f'the factorial is: {factorial(5)}')

x = 10
y= 20
sum2 = lambda x,y: x+y
print(f'{sum2(x,y)}')