import constants
key = 3
message = 'ABCD EFGHIJKLMNOPQRSTUVW XYZ'
def coder(message, key):
    res = ''
    for char in message.lower():
        char_index = ord(char)
        if char_index == 32:
            res += char
            continue
        new_Index = char_index + key
        if new_Index > 122:
            offset = new_Index - 122
            new_Index = 96 + offset
        res += chr(new_Index)
    return res.upper()

def reverse(message):
    res = ''
    for char in message:
        res = char + res
    return res
    
def fingilish(word):
    res = ''
    for char in word:
        if not constants.PersianDict[char]:
             res += char
             continue
        res += constants.PersianDict[char]
            
       
    return res

print (coder(message, key))
print (reverse(message))
print (fingilish('فارسی'))