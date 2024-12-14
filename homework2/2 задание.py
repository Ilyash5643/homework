from collections import deque
first_list = deque([1,3,5,7])
second_list = deque([2,4,6,8])
deque = sorted((first_list + second_list))
print(deque)
