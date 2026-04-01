votes = ['Alice', 'Bob', 'Alice', 'Carol', 'Bob', 'Alice', 'Carol', 'Bob', 'Alice']
b={}
for i in votes:
    b[i]=b.get(i,0)+1
ma=0
for key,value in b.items():
    if value>ma:
        ma=value
        c=key
print(c,ma,sep=" : ")