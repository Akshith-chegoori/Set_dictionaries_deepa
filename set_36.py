marks = [72, 85, 72, 91, 85, 60, 91, 55, 72]
d={}
for i in marks:
    d[i]=d.get(i,0)+1
print(d,len(set(marks)))