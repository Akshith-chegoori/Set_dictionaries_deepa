prices = {'apple': 40, 'banana': 20, 'mango': 80, 'grapes': 60}
d={}
for key,value in prices.items():
    d[key]=1.1*value
print(d)