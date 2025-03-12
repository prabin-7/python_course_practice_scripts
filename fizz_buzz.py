if __name__ == "__main__":
    number = 10

    if number % 3 ==0 and number % 5 == 0:  # this should be at first so that number like 15 doesnot give only fizz
        print("fizzbuzz")

    elif number % 3 ==0: 
        print("fizz")
    elif number % 5 ==0:
        print("buzz")

    else: 
        print(number)