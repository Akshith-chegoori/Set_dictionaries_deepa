# Three friends each have a set of movies they have watched:
a= {'Inception', 'Interstellar', 'Dune', 'Oppenheimer'}
b= {'Dune', 'Tenet', 'Inception', 'Avatar'}
c= {'Interstellar', 'Dune', 'Gravity', 'Inception'}
#Movies all three have watched
#use intersection() or & between sets
r=a.intersection(b,c)
print(f"Movies all three have watched are:{r}")
#we get same output as above by performing below code
r=a&b&c
print(r)











#Movies watched by Alice and Bob but not Carol
r1=(a&b)-c
if len(r1)==0:
    print("Movies watched by Alice and Bob but not Carol none")
else:
    print(f"Movies watched by Alice and Bob but not Carol:{r1}")
