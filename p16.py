


a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
#Are these two sets disjoint? Write code to check and print a meaningful message.
#if intersection is zero then the sets are disjoint
d=a.intersection(b)

if len(d)==0:
    print("the given sets are disjoint")
else:
    print("the given sets are not disjoint")
