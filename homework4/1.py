def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = int(input())
fib_chisla = list(fib(n))
print(fib_chisla)
