# used to find out circumference and area of circle

class circle():
    def __init__(self,r):
        self.radius = r
    
    def area(self):
        return self.radius*self.radius*3.14
    
    def circumference(self):
        return 2*3.14*self.radius

rad = int(input("Enter the radius of the circle: "))

NewCircle = circle(rad)
print("The area of the circle is: ")
print(NewCircle.area())
print("The circumference of the circle is: ")
print(NewCircle.circumference())
