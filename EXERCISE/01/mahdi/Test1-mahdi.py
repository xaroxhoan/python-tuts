def coder(word, key):
    new_word = []
    a = ''
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for each_chr in word:
        index = (alfabet.index(each_chr) + key) % 26
        new_word.append(alfabet[index])
    a = a.join(new_word)
    return a

word = input('kalame ra wared konid:  ')
key = int(input('key ra wared konid:   '))

new_word = coder(word, key)

print('kalame ramz shode:   ', new_word)