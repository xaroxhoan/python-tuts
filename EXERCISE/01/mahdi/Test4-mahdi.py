def f(n):
    donbale_n = []
    for i in range(1 ,int(n)+1):
        donbale_n.append(i)

    donbale = []
    repeat = 2
    for i in donbale_n:
        if i == 1:
            donbale.append(1)
        elif i == 2:
            donbale.append(2)
            donbale.append(2)
        else:
            donbale.append(i)
            x = donbale.count(donbale[-1])
            while x < repeat:
                donbale.append(donbale[-1])
                x += 1

            repeat = donbale[i]
    index = donbale[int(n) - 1]
                
    return index

n = input('N ra vared konid:   ')

tekrar = f(n)

print('F(n) = ', tekrar)
