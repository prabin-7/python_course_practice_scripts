ex_group = ExceptionGroup(
    'this is an exception group',(ValueError('this is a value error1'),ValueError('this is a value error2')
                                  , TypeError('this is a type error'),ValueError('this is a value error3'))
)

try: 
    raise ex_group
except* ValueError as e:
    # print(e.exceptions)     #this one gives all the ValueErrors and [0] GIVES THE MESSAGE OF THE SPECIFIC EXCEPTION
    print(e.exceptions[1])           #the tuple of only one type of exception is made and can be accessed throuh the indexing operation it gives the 3 gives the third exception ValueError as it is done for e.exceptions[2]
except* TypeError as e: 
    print(e.exceptions)