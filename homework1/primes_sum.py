sum = 0
for number in range(2, int(input('Введите число')) + 1):
    check = True
    for delitel in range(2, number):
        if number % delitel == 0:
            check = False
            continue
    if check:
        sum += number
print(sum)