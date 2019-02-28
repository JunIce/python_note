#coding=utf-8
import math

class Point:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0,0)
    def distance(self, o):
        return math.sqrt(
            (self.x - o.x)**2 +
            (self.y - o.y)**2
        )

a = Point()
b = Point()
a.move(1,1)
b.move(1,5)
print(a.distance(b))
z = 'hello world'
print(z.title())
print('orz' in z)
