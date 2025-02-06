import math
# Example of constructors: int() float() list() dict() ...

class Point: # predefined special methods: __new__() __init__() __repr__() __eq__()
    def __init__(self, valx=0, valy=0):
        self.x=valx # x is an "attribute"
        self.y=valy # y is an "attribute"
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self,other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        if isinstance(other, int):
            return Point(self.x+other, self.y+other)
        raise Exception("Wrong operand used with the + operator ")
    def __eq__(self, other):
       return self.x == other.x and self.y == other.y 
    def distance(self, other):
        """
        It is calculated by the formula Sqrt(x2 − x1)2 + (y2 − y1)2).
        """
        return math.sqrt((other.x - self.x)**2 +(other.y - self.y)**2)

center=Point()
print(center)

p1=Point(2,3)
# 1) p1=p1.__new__()
# 2) p1.__init__(2,3) <===
# 3) __init__(p1,2,3)

print(p1) # <2,3>
# print(p1.__repr__())

print(p1.x) # 2
print(p1.y) # 3

p2=Point(3,4)
print(p2) # <3,4>
p2.x=5
print(p2) # <5,4>

p3=p1+p2
# 1) p3=p1.__add__(p2))
# 2) p3=__add__(p1,p2)
print(p3) # <7,7>
p5=p1+10
# 1) p5=p1.__add__(10))
# 2) p5=__add__(p1,10)

print(p5)

p4=Point(2,3)
print(p1,p4)
if p1 == p4:
    print("p1 is equal to p4")
else:
    print("p1 is different from p4")

result=p2.distance(p4)
print("distance between p2 and p4",result)


