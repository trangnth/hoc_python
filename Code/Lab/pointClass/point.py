'''
Xây dựng class cho đối tưởng Điểm trong hệ truc toan đô Oxy
Class gồm các method:
+ Tính khoảng cách từ điểm đó đến điểm khác
+ Reset: đặt điểm đó về gốc tọa độ
+ Tính cosin của góc tạo bởi đường thẳng đi qua đường thẳng đó và một điểm khác với trục hoành
+ Scale: gấp x lần tọa độ hoành và y lần tọa độ tung
'''

from math import sqrt

class Point:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def resetPoint(self):
		self.x = 0
		self.y = 0

	def scale(self, a, b):
		self.x *= a
		self.y *= b

	def showPoint(self): 
		print("x =", self.x)
		print('y =',self.y)

	def distancePoint(self, p):
		return (sqrt((self.x - p.x)**2 + (self.y - p.y)**2))

	def cosinPoint(self, d):
		if self.x == d.x and self.y == d.y:
			return False
		elif self.x == d.x:
			return 0
		elif self.y == d.y:
			return 1
		else:
			dist = sqrt((self.x - d.x)**2 + (self.y - d.y)**2)
			return (abs(self.x - d.x) / dist)
