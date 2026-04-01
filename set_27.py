dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4, 'e': 5}
d3={}
for key,value in dict2.items():
    dict1[key]=value
print(dict1)