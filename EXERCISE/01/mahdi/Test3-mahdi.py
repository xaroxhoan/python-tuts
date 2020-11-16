def finglish(word):
    new_word = ''
    for chr in word:
        new_word += PersianDict[chr]
    return new_word

PersianDict = {
    'ا': 'a' ,
    'ب': 'b' ,
    'پ': 'p' ,
    'ت': 't' ,
    'ث': 's' ,
    'ج': 'j' ,
    'چ': 'ch' ,
    'ح': 'h' ,
    'خ': 'kh' ,
    'د': 'd' ,
    'ذ': 'z' ,
    'ر': 'r' ,
    'ز': 'z' ,
    'ژ': 'zh' ,
    'س': 's' ,
    'ش': 'sh' ,
    'ص': 's' ,
    'ض': 'z' ,
    'ط': 't' ,
    'ظ': 'z' ,
    'ع': 'a' ,
    'غ': 'gh' ,
    'ف': 'f' ,
    'ق': 'gh' ,
    'ک': 'k' ,
    'گ': 'g' ,
    'ل': 'l' ,
    'م': 'm' ,
    'ن': 'n' ,
    'و': 'oo' ,
    'ه': 'h' ,
    'ی': 'i' ,
}

word = input('word:   ')
new_word = finglish(word)
print(new_word)