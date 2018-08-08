'''
Xây dựng class hinh chữ nhật:
+ check xem có phải hình hcn ko
+ Tính chu vi
+ Tính diện tích
+ Class hình vuông, kế thừa từ class hình chữ nhật, cũng có các thuộc tính tương tự

'''

from point import Point
from math import sqrt

class Rectangle :  
    def __init__(self, p1, p2, p3, p4): 
        listPoint = [p1, p2, p3, p4]
        self.listDist = []

        for i, x in enumerate(listPoint):
            for j in range(i+1, 4):
                self.listDist.append(x.distancePoint(listPoint[j]))               
        self.listDist.sort()

    def isRect(self):        
        for i in range(0,6,2):
            if self.listDist[i] != self.listDist[i+1]:
                return False
        return True

    def getLength(self):
        if self.isRect():
            return self.listDist[2]
        # else:
        #     raise Exception('It is not Rectangle.')

    def getWidth(self):
        if self.isRect():
            return self.listDist[0]
        # else:
        #     raise Exception('It is not Rectangle.')

    def area(self):
        return self.getLength() * self.getWidth()

    def perimeter(self):
        return (self.getLength() + self.getWidth())*2


class Square(Rectangle):
    def isSquare(self):
            if self.getLength() == self.getWidth():
                return True


def main():
    
    p1 = Point(1,4)
    p2 = Point(5,4)
    p3 = Point(5,2)
    p4 = Point(1,2)

    r1 = Rectangle(p1, p2, p3, p4)

    p5 = Point(1, 3)
    p6 = Point(1, 1)
    p7 = Point(3, 3)
    p8 = Point(3, 1)

    r2 = Square(p8, p5, p6, p7)

    r3 = Rectangle(p1, p2, p4, p7)
    r3.getLength()

    try:
        print(r3.getLength())
        r3.area()
    except:
        print("It is not rectangle.")

    if r1.isRect() == True:
        print("width =", r1.getWidth())
        print("height =", r1.getLength())
        print("Area: ", r1.area())
        print("Perimeter: ", r1.perimeter())
    else:
        print("r1 is not rectangle.")

    print("================")

    if r2.isSquare() == True:  
        print("width =", r2.getWidth())
        print("Area: ", r2.area())
        print("Perimeter: ", r2.perimeter())
    else:
        print("r2 is not square.")

 
if __name__ == "__main__":
    main()
