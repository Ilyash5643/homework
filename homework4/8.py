def num(mass):
    for i in mass:
        if len(i) > 3:
            yield i

mass = ['1, 2, 3, 4, 5', '1', 'dfs', 'dsfk']
check = num(mass)
print(list(check))