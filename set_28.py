d = {'x': 10, 'y': 20, 'z': 30}
d.pop('y')
print(d)
print(d.pop('a', 'Key missing'))
print(len(d))
