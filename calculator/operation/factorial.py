from model.operation import IOperation


class Factorial(IOperation):
    
    def __init__(self, operand):
        self.__operand = operand
        
    def operate(self) -> str:
        result = 1
        for i in range(1, self.__operand + 1):
            result *= i
            
        return f'{self.__operand}! = {result}'