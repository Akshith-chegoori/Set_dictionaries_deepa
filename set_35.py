nums = [1, 2, 3, 4, 5]
d={}
c={}
for i in nums:
    d[i]=i**2
for key , value in d.items():
    if value>10:
        c[key]=value
print(d)
print(c)