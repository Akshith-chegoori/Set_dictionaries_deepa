#Find students who are in exactly one subject — not both. Which operation gives this? Write the code.
ps={'Ravi', 'Priya', 'Arjun', 'Meena', 'Kiran'}
js={'Priya', 'Kiran', 'Sneha', 'Rohit', 'Arjun'}

#use symmetric_difference or ^ operator
#consider set a and set b we  perform (a-b)union(b-a)
en1=ps^js
print(f"the students who are in exactly one subject — not both:{en1}")

#we get same output as above by performing below code
en2=ps.symmetric_difference(js)
print(en2)

