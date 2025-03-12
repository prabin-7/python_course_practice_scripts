if __name__ == "__main__": 
    operation = input("Enter the operation(add,sub,mul,div):").lower()
    num1 = int(input('enter the first number:'))
    num2 = int(input('enter the second number:'))

    match operation:
        case 'add':
            results = num1+num2
        case 'sub':
            results = num1-num2
        case 'mul':
            results = num1 * num2
        case 'div':
            results = num1 / num2
        case _ :
            result = -1
            print('invalid input operation')

    print("Result:", results)


 

