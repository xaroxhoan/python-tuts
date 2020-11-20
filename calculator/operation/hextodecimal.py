from model.operation import IOperation


class HexToDecimal(IOperation):
    
    def __init__(self, operand):
        self.__operand = operand
        
    def oprand(self) -> str:
        return f'decimal({int(str(self.__operand), 16)})'