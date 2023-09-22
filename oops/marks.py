class marks:
    def __init__(self):
        self.mark1 = 0
        self.mark2 = 0
        self.mark3 = 0
    def inMark(self):
        self.mark1=int(input("mark 1 :"))
        self.mark2 = int(input("mark 2 :"))
        self.mark3 = int(input("mark 3 :"))
    def sumOfMark(self):
        self.sum = self.mark1+self.mark2+self.mark3
        return self.sum
    def avgOfMark(self):
        self.avg = (self.mark1+self.mark2+self.mark3)//3
        return self.avg


