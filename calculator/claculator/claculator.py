from operation.addition import Addition
from operation.subtraction import Subtraction


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