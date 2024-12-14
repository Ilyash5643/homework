def gen(s):
    check = set()
    for i in s:
        if i not in check and i != ' ':
            check.add(i)
            yield i

test = 'мама съела кашу'
test1 = gen(test)
print(list(test1))
