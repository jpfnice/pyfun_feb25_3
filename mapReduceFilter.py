"""
map(function, iterable)
filter(function, iterable)
reduce(function, iterable) (import functools)

"""

data=[3,5,-1,7,-2,7,-12,100]

newlist=[]
for e in data:
    newlist.append(e**3)

print("new list is", newlist)

def pow3(a):
    return a**3

newlist=list(map(pow3, data))
print("new list is", newlist)

text="23:67:78:89:90:10"
numbers=list(map(int, text.split(":")))
print(numbers)

data=[3,5,-1,7,-2,7,-12,100,54,23]

def even(nb):# -> bool
    return nb % 2 == 0

def odd(nb):# -> bool
    return nb % 2 != 0

newlist=list(filter(even, data))
print("new list is", newlist)

newlist=list(filter(odd, data))
print("new list is", newlist)

def mult(a,b):
    return a*b

import functools
result=functools.reduce(mult, data)
print(result)
