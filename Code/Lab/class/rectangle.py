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
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def isRect(self):
        if self.p1.distancePoint(self.p2) != self.p3.distancePoint(self.p4):
            return False
        elif self.p1.distancePoint(self.p3) != self.p2.distancePoint(self.p4):
            return False
        elif self.p1.distancePoint(self.p4) != self.p3.distancePoint(self.p2):
            return False
        else:
            self.height = min(self.p1.distancePoint(self.p2), self.p1.distancePoint(self.p3), self.p1.distancePoint(self.p4))
            d = max(self.p1.distancePoint(self.p2), self.p1.distancePoint(self.p3), self.p1.distancePoint(self.p4))
            self.width = round(sqrt(d**2 - self.height**2),1)
            return True

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height)*2

class Square(Rectangle):

    def isSquare(self):
        if self.isRect() == True:
            if self.getWidth() == self.getHeight():
                return True
        else:
            return False

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

    if r1.isRect() == True:
        print ("width =", r1.getWidth())
        print("height =", r1.getHeight())
        print("Area: ", r1.area())
        print("Perimeter: ", r1.perimeter())
        #print(Rectangle.width)

    else:
        print("r1 is not rectangle.")

    print("================")

    if r2.isSquare() == True:
        print("height =", r2.getHeight())
        print("Area: ", r2.area())
        print("Perimeter: ", r2.perimeter())
    else:
        print("r2 is not square.")

 
if __name__ == "__main__":
    main()
