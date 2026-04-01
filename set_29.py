Ravi1={'Roll':101,'Marks':72,'Grade':'B'}
Priya1={'Roll':102,'Marks':91,'Grade':'A'}
Arjun1={'Roll':103,'Marks':65,'Grade':'C'}
doo={'Ravi':Ravi1,'Priya':Priya1,'Arjun':Arjun1}
doo['Arjun1']['Marks']=70
print(doo['Priya']['Grade'])
print(doo)