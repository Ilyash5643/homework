def generator():
    i = yield
    while True:
        if i >= 0:
            i = yield i ** 0.5
        else:
            i = yield None

gen = generator()
next(gen)
numbers = [1, -1, 2, -1, 3, 4, -1, -2, -3, 4]
for i in numbers:
    result = gen.send(i)
    result = gen.send(i)
    if result is not None:
        print(result)