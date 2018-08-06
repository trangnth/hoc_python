from point import Point

p1 = Point(1,1)
p2 = Point(4,3)
p3 = Point(3,4)

p1.showPoint()

p2.scale(2,3)
p2.showPoint()

p1.resetPoint()
p1.showPoint()

print(p2.distancePoint(p3))
print(p1.cosinPoint(p2))