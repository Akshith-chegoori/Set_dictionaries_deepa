original = {'a': 1, 'b': 2, 'c': 3}
d={}
for key ,value in original.items():
    d[value]=key
print(d)