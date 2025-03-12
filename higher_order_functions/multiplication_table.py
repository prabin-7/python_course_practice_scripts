from typing import Callable
#outer and inner fxn defination
def multiplier(fact:int) -> Callable[[list[int]],list[int]]:
    def multiply_by(lst: list):
        return [fact*num for num in lst]
    return multiply_by

#creating closures that has params needed for outer fxn
tens = multiplier(10)
double = multiplier(2)


lst_1 = [x for x in range(10) if x%2 == 0]

#calling closures with the remaining values req for the execution of the inner functions
results1 = tens(lst_1)
results2 = double(lst_1)
print(results1,results2)