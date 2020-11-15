def f(n):
    donbale = []
    repeat = 2
    for i in n:
        if int(i) == 1:
            donbale.append(1)
        elif int(i) == 2:
            donbale.append(2)
        else:
            donbale.append(int(i))
            x = donbale.count(donbale[-1])
            while x < repeat:
                donbale.append(donbale[-1])
                x += 1

            repeat = donbale[int(i)-1]
            
            
            
    return donbale

n = input('donbale adad ra vared konid:(mesal: 1 2 3 4)   ')
n = n.split(' ')

donbale = f(n)

print('F(n) = ', donbale)