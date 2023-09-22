class circle:
    def __init__(self):
        self.radius = 0
    def setRadius(self,r):
        self.radius=r
    def area(self):
        self.areaOfcircle = 3.142*(self.radius*self.radius)
    def circum(self):
        self.circumOfCircle = 2*3.142*self.radius
    def displayItem(self):
        print("area of circle",self.areaOfcircle)
        print("circumference of circle", self.circumOfCircle)
