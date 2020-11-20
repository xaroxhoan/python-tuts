from model.operation import IOperation


class DecimalToHex(IOperation):
    
    def __init__(self, operand):
        self.__operand = operand
        
    def operate(self) -> str:
        result = format(self.__operand, '02x')
        return f'Hex({self.__operand}) = {result}'