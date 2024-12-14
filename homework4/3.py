def generator(dlina):
    if dlina == 0:
        yield ""
    else:
        for i in generator(dlina - 1):
            yield i + "a"
            yield i + "b"
def check(dlina):
    sum = 0
    for i in generator(dlina):
        if "ab" not in i:
            sum += 1
    return sum
dlina = 6
itog = check(dlina)
print(itog)
