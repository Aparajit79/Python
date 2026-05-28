import math

class shapes:
  def area(self):
   return
  
class rectangle(shapes):
  def __init__(self,width,heigth):
     self.width = width
     self.heigth = heigth

  def area(self):
    return self.width * self.heigth
  

class circle(shapes):
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return math.pi * (self.radius ** 2)
  

rect = rectangle(10,20)
circ = circle(10)

print(f"Area of circle : {circ.area():.2f}")
print(f"Area of Rectangle : {rect.area()}")
