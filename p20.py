# What is the output? Explain the difference between the two access methods:
d = {'name': 'Ravi', 'age': 20}
print(d['name'])#this prints the value stored in key mentioned in []
print(d.get('age'))#same as above but get()
print(d.get('city'))
print(d.get('city', 'Not found'))



#d[] prints the value stored in it otherwise it gives error, but get() prints none as default if that key is not present in dict or we can give any statement by seperating it with ,


