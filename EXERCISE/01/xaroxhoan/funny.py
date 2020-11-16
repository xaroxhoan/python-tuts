def funny(input):
    output = [1, 2]
    for index in range(1, input + 1):
        occurrence = output.count(index)
        while occurrence < output[index - 1]:
            output.append(index)
            occurrence = output.count(index)
    return output[input - 1]


w = input('Insert n to get F(n): ')
print(funny(int(w)))
