def power(a, n):
    if n >= 1:
        return a * power(a, n - 1)
    else:
        return 1

