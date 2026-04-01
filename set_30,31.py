students = {
    'Ravi':  {'marks': 72, 'branch': 'CSE'},
    'Priya': {'marks': 91, 'branch': 'ECE'},
    'Arjun': {'marks': 65, 'branch': 'CSE'},
    'Meena': {'marks': 85, 'branch': 'CSE'}
}
s=0
ma=0
for key,value in students.items():
    print(key)
    s=s+value['marks']
    if value['marks']>ma:
        ma=value['marks']
        rrr=key
print(f"Maximum marks of {ma} is scored by {rrr}")
print(f"average of all students is {s/len(students)}")
students['Kiran']={'marks':78,'branch':'Ece'}
students.pop('Arjun')
print(students)