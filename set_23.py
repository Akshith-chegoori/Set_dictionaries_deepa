inventory = {'pen': 50, 'book': 30, 'eraser': 80, 'ruler': 20}
ma=0
mi=1000000
t=0
for key,value in inventory.items():
    if value>ma:
        ma=value
        a=key
    if value<mi:
        mi=value
        b=key
    t+=value
print(a,ma,sep=" : ")
print(b,mi,sep=" : ")
print(t)