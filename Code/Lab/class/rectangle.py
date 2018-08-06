'''
Xây dựng class hinh chữ nhật:
+ check xem có phải hình hcn ko
+ Tính chu vi
+ Tính diện tích
+ Class hình vuông, kế thừa từ class hình chữ nhật, cũng có các thuộc tính tương tự

'''

from point import Point

class Rectangle :
	width = 0
	height = 0
	def __init__(self, p1, p2, p3, p4):       
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


    def isRect(self):
    	if self.p1 == self.p2 or self.p1 == self.p3 or self.p1 == self.p4 or self.p2 == self.p3 or self.p2 == self.p4 or self.p3 == self.p4:
    		return False
    	elif self.p1.x == self.p4.x and self.p1.y == self.p2.y and self.p2.x == self.p3.x and self.p3.y == self.p4.y:
    		
    		if (self.p2.x - self.p1.x) >= (self.p1.y - self.p4.y):
		    	self.width = self.p2.x - self.p1.x
		    	self.height = self.p1.y - self.p4.y
		    else:
		    	self.width = self.p1.y - self.p4.y
		    	self.height = self.p2.x - self.p1.x
		    return True
    	else:
    		print(p4.x)
    		return False

    def getWidth(self):
    	return self.width

    def getHeight(self):
    	return self.height

    def areaRect(self):
        return self.width * self.height

    def perimeterRect(self):
    	return (self.width + self.height)*2

def main():
	# 4 diem khai bao lan luot theo thu tu chieu kim dong ho
    p1 = Point(1,4)
    p2 = Point(5,4)
    p3 = Point(5,2)
    p4 = Point(1,2)
    r1 = Rectangle(p1, p2, p3, p4)

    if r1.isRect() == True:
    	print ("width =", r1.getWidth())
    	print("height =", r1.getHeight())
    	print("Dien tich: ", r1.areaRect())
    	print("Chu vi: ", r1.perimeterRect())

    else:
    	print("r1 is not rectangle.")

if __name__ == "__main__":
    main()
