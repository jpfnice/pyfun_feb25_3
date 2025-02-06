"""
Write a Stack class using a composition mechanism (the Stack class will use internally the List class).
The Stack class should offer the following facilities:
    a push() method to add an element on top of the Stack
    a pop() method to get and remove the element on top of the Stack
    a peek() method to get the element on top of the Stack
    a way to determine its size (its current number of elements),
    a way to print easily the content of the Stack
    a way to test if an element belongs to the stack or not
    
Name of the method to provide:
    
    push(self,element) -> None
    pop(self) -> element
    peek(self) -> element
    __len__(self) -> int
    __repr__(self) -> str
    __contains__(self) -> bool
    __init__(self,mSize) -> None
    
Name of the attributes to provide:
    maxSize -> int
    content -> list
    
"""

s1=Stack(12) # 12 is the maxmimum size of the Stack s1

# d=[7,8,8]
# print(len(d)) # print(d.__len__())

