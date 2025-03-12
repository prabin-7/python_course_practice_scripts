class InvalidAgeError(Exception):
    def __init__(self,age, message):
        self.message = message
        self.age = age
        super().__init__(self.message)

#now write the working of the function that produces exception
def validate_age(age):
    if age <0 :
        raise InvalidAgeError(age,'Age cannot be negative')
    if age>120:
        raise InvalidAgeError(age, 'Age cannot be gerater than 120')
    return age
try:
    validate_age(10)
    validate_age(-4)
               #this line is never executed as the above one raises an exception

except InvalidAgeError as e:
    print(f'Exception found: {e.message}')
else:
    print(f'{age} is valide age')
finally:
    print(f'the block is done')
print('hello world')          
validate_age(200)      
'''so only the try-except-else-finally block's execution is hampered by the exception and not the following 
after the try-except-else-finally block'''    #doc-strins!!
