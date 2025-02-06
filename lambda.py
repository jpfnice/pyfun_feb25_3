"""
lambda expression
"""

data=[3,5,-1,7,-2,7,-12,100]

# def pow3(a):
#     return a**3

# lambda parameters:expression

newlist=list(map(lambda a:a**3, data))
print("new list is", newlist)

text="23:67:78:89:90:10"
numbers=list(map(int, text.split(":")))
print(numbers)

data=[3,5,-1,7,-2,7,-12,100,54,23]

# def text(nb):# -> bool
#     return nb % 2 == 0

# def odd(nb):# -> bool
#     return nb % 2 != 0

newlist=list(filter(lambda nb:nb%2==0, data))
print("new list is", newlist)

newlist=list(filter(lambda nb:nb%2!=0, data))
print("new list is", newlist)

# def mult(a,b):
#     return a*b

import functools
result=functools.reduce(lambda a,b:a*b, data)
print(result)
