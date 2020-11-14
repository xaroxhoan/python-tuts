def str_reverser(word):
    index = len(word)
    a = []
    new_word = ''
    i = 1
    while i <= index:
        new_index = index - i
        a.append(word[new_index])
        i += 1
    new_word = new_word.join(a)
    return new_word

word = input('kalame ra vared konid:  ')
new_word = str_reverser(word)
print(new_word)