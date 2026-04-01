data = [5, 3, 8, 3, 9, 5, 1, 8, 2]
da=set(data)
for i in da:
    print(i,end=" ")
print(f"\n{len(data)-len(da)}")
print(sorted(list(da)))

