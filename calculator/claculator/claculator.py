from operation.addition import Addition
from operation.subtraction import Subtraction
from operation.hextodecimal import HexToDecimal
from operation.decimaltohex import DecimalToHex
from operation.multiply import Multiply
from operation.divide import Divide
from operation.factorial import Factorial
from operation.remain import Remain


class Calculator:

    def __init__(self):
        self.__memory = []

    def memory(self):
        if len(self.__memory) != 0:
            print(self.__memory.pop().operate())
        else:
            print('There is no operation to show')

    def clear(self):
        self.__memory.clear()
        print('clearing done')

    def add(self, operand1, operand2):
        instance = Addition(operand1, operand2)
        self.__memory.append(instance)
        print(instance.operate())

    def subtract(self, operand1, operand2):
        instance = Subtraction(operand1, operand2)
        self.__memory.append(instance)
        print(instance.operate())
        
    def hextodecimal(self, operand):
        instance = HexToDecimal(operand)
        self.__memory.append(instance)
        print(instance.operate())
        
    def decimaltohex(self, operand):
        instance = DecimalToHex(operand)
        self.__memory.append(instance)
        print(instance.operate())
        
    def multiply(self, operand1, operand2):
        instance = Multiply(operand1, operand2)
        self.__memory.append(instance)
        print(instance.operate())
        
    def divide(self, operand1, operand2):
        instance = Divide(operand1, operand2)
        self.__memory.append(instance)
        print(instance.operate())
        
    def factorial(self, operand):
        instance = Factorial(operand)
        self.__memory.append(instance)
        print(instance.operate())
        
    def remain(self, operand1, operand2):
        instance = Remain(operand1, operand2)
        self.__memory.append(instance)
        print(instance.operate())
