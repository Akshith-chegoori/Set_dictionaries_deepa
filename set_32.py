marks = {'Ravi': 72, 'Priya': 91, 'Arjun': 65, 'Meena': 85, 'Kiran': 48}
d={}
for key, value in marks.items():
    if value>=50:
        d[key]=value
print(d)