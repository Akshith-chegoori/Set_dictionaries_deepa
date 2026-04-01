roster_a = ['Ravi', 'Priya', 'Arjun', 'Meena']
roster_b = ['Priya', 'Kiran', 'Arjun', 'Sneha']
b= set(roster_a) & set(roster_b)
l={}
for i in list(b):
    l[i]=2    
print(l)    