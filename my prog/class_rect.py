class rect:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
print("The area is: ")

rectangle = rect(l,b)
print(rectangle.area())
