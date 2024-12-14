def merge_dicts(dict1, dict2):
    merge = {}
    for key, value in dict1.items():
        merge[key] = value
    for key, value in dict2.items():
        if key in merge:
            merge[key] = [merge[key], value]
        else:
            merge[key] = value
    return merge

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

a = merge_dicts(dict1, dict2)
print(a)
