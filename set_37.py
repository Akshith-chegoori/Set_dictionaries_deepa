a="she sells seashells by the seashore"
c=set(a)
ff={}
for i in a:
    ff[i]=ff.get(i,0)+1
print(ff)
ma=0
for key, value in ff.items():
    if value>ma:
        ma=value
        zoo=key
print(f"The highest reoccuring is {zoo}")