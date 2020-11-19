class Calculator:
    memory = []
    
    def add(self, a, b):
        result = a + b
        Calculator.memory.append('%i + %i = %i' % (a, b, result))
        print(Calculator.memory[-1])
    
    def subtract(self, a, b):
        result = a - b
        Calculator.memory.append('%i - %i = %i' % (a, b, result))
        print('%i - %i = %i' % (a, b, result))
    
    def multiply(self, a, b):
        result = a * b
        Calculator.memory.append('%i * %i = %i' % (a, b, result))
        print('%i * %i = %i' % (a, b, result))
    
    def divide(self, a, b):
        result = a / b
        Calculator.memory.append('%i / %i = %i' % (a, b, result))
        print('%i / %i = %i' % (a, b, result))    
    
    def remain(self, a, b):
        result = a % b
        Calculator.memory.append(result)
        print('%i bachimande bar %i = %i' % (a, b, result))    
    
    def fact(self, a):
        result = 1
        for i in range(1, a + 1):
            result *= i
        Calculator.memory.append('%i! = %i' % (a, result))
        print('%i! = %i' % (a, result))
        
    def Memory(self):
        if len(Calculator.memory) == 0:
            print('no opration saved in memory!')
        else:
            print(Calculator.memory[-1])
            Calculator.memory.pop()
        
        
calcul = Calculator()

print(calcul.add(2,5))
print(calcul.subtract(10, 6))
print(calcul.multiply(4, 5))
print(calcul.divide(10, 5))
print(calcul.remain(13, 2))
print(calcul.fact(4))
print(calcul.Memory())
print(calcul.Memory())
print(calcul.Memory())
print(calcul.Memory())
print(calcul.Memory())
print(calcul.Memory())
print(calcul.Memory())