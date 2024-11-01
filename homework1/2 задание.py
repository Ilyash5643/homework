line = input('Введите текст')
if line == line[::-1]:
    print('Эта строка - палиндром')
else:
    print('Эта строка не палиндром')