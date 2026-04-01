
ps={'Ravi', 'Priya', 'Arjun', 'Meena', 'Kiran'}
js={'Priya', 'Kiran', 'Sneha', 'Rohit', 'Arjun'}




#Find students enrolled in Python but not in Java. 
#use - or difference()
en=ps-js
print(f"the students enrolled in python but not in java:{en}")
#we get same output as above by performing below code
en=ps.difference(js)
print(en)







# Then find students in Java but not in Python.
#use - or difference()

en1=js-ps
print(f"the students enrolled in java but not in python:{en1}")
#we get same output as above by performing below code
en1=js.difference(ps)
print(en1)