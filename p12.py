#Find students who are enrolled in both Python and Java. Which operation is this?
ps={'Ravi', 'Priya', 'Arjun', 'Meena', 'Kiran'}
js={'Priya', 'Kiran', 'Sneha', 'Rohit', 'Arjun'}
#use intersection() or &
en=ps.intersection(js)
print(f"the students enrolled in both python and java:{en}")
#we get same output as above by performing below code
en=ps&js
print(en)