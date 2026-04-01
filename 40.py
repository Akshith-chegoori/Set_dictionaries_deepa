library = {
    'Ravi':  ['Python Basics', 'DSA', 'DBMS'],
    'Priya': ['OS', 'Python Basics', 'Networks'],
    'Arjun': ['DSA', 'OS', 'Python Basics']
}
print(set(library['Ravi'] )| set(library['Arjun']) | set(library['Priya']))
print("students who have the book DSA")
if 'DSA' in library['Arjun']:
    print("Arjun",end=" ")
if 'DSA' in library['Priya']:
    print('Priya',end=" ")
if 'DSA' in library['Ravi']       :
    print('Ravi')
b=set(library['Ravi'] ) & set(library['Arjun']) & set(library['Priya'])    
if (len(b)!=0):
    print("nalla")
    print(b)
else :
    c= set(library['Ravi']).intersection(set(library['Arjun'])) + set(library['Ravi']).intersection(set(library['Priya']))+set(library['Priya']).intersection(set(library['Arjun']))
    print(c)        