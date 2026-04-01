b=[]
while True:
   a=input("city name or (q to quit )")
   if (a.lower()=='q'):
       break
   else:
       b.append(a)
b=list(set(b))
print(sorted(b))        
   