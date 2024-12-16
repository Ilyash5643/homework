from collections import deque


size = 10
hash_table = [[] for i in range(size)]

def hash_function(j):
    return len(j) % size
keys = ["hello", "world", "hi", "Python", "hash"]
for j in keys:
    index = hash_function(j)
    if not hash_table[index]:
        hash_table[index] = deque()
    if j not in hash_table[index]:
        hash_table[index].append(j)
