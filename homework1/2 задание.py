line = input()
left = 0
right = len(line) - 1
check = True
while left < right:
    if line[left] != line[right]:
        check = False
        break
    left += 1
    right -= 1
if check:
    print('Эта строка - палиндром')
else:
    print('Эта строка не палиндром')
