from model.operation import IOperation


class HexToDecimal(IOperation):
    
    def __init__(self, operand):
        self.__operand = operand
        
    def operate(self) -> str:
        result = int(str(self.__operand), 16)
        return f'decimal({self.__operand}) = {result}'