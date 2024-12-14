def num(mass):
    for i in mass:
        if i % 2 == 0:
            yield i

mass = [1, 2, 3, 4, 5]
check = num(mass)
print(list(check))