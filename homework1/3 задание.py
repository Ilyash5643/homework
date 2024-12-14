stack = ["2", "1", "+", "3", "*"]
help_massiv = []
check = True
for element_num in range(len(stack)):
    if stack[element_num] == '/':
        help_massiv.append(int(help_massiv[len(help_massiv) - 2]) // int(help_massiv[len(help_massiv) - 1]))
        help_massiv.pop(len(help_massiv) - 2)
        help_massiv.pop(len(help_massiv) - 2)
        continue
    elif stack[element_num] == '+':
        help_massiv.append(int(help_massiv[len(help_massiv) - 2]) + int(help_massiv[len(help_massiv) - 1]))
        help_massiv.pop(len(help_massiv) - 2)
        help_massiv.pop(len(help_massiv) - 2)
    elif stack[element_num] == '*':
        help_massiv.append(int(help_massiv[len(help_massiv) - 2]) * int(help_massiv[len(help_massiv) - 1]))
        help_massiv.pop(len(help_massiv) - 2)
        help_massiv.pop(len(help_massiv) - 2)
    elif stack[element_num] == '-':
        help_massiv.append(int(help_massiv[len(help_massiv) - 2]) - int(help_massiv[len(help_massiv) - 1]))
        help_massiv.pop(len(help_massiv) - 2)
        help_massiv.pop(len(help_massiv) - 2)
    else:
        help_massiv.append(stack[element_num])
print(help_massiv)
