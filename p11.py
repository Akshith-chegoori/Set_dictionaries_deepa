#Find all students who are enrolled in either Python or Java (or both). Which set operation do you use?


ps={'Ravi', 'Priya', 'Arjun', 'Meena', 'Kiran'}
js={'Priya', 'Kiran', 'Sneha', 'Rohit', 'Arjun'}
#use union() or |
en=ps.union(js)
print(f"the students enrolled in either Python or Java ={en}")
#we get same output as above by performing below code
en=ps|js
print(en)