string = input()
helper = {')': '(',
     ']': '[',
     '}': '{'}
helper_1 = []
for skobka in string:
    if skobka in helper.values():
        helper_1.append(skobka)
    elif skobka in helper.keys():
        if helper_1 == [] or helper[skobka] != helper_1.pop():
            print('False')
            exit()
print('True')