
data=[3,5,-1,7,-2,7,-12,100]

# Version 1:
newlist=[]
for e in data:
    newlist.append(e**3)
print("new list is", newlist)


# Version 2:
newlist=[e**3 for e in data] # A "list comprehension" example
print("new list is", newlist)


# Version 1:
newlist=[]
for e in data:
    if e > 0:
        newlist.append(e**3)
print("new list is", newlist)


# Version 2:
newlist=[e**3 for e in data if e > 0] # A "list comprehension" example
print("new list is", newlist)

# data=[2*2, 3**2, ...., 10**2]

data=[nb**2 for nb in range(2,11)]
print(data)





