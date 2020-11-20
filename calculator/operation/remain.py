from model.operation import IOperation


class Remain(IOperation):
    
    def __init__(self, operand1, operand2):
        self.__operand1 = operand1
        self.__operand2 = operand2
        
    def operate(self) -> str:
        return f'{self.__operand1} % {self.__operand2} = {self.__operand1 % self.__operand2}'