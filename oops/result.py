class result:
    def input(self):
        self.rollno = input("rollnum: ")
        self.name = input("name: ")
        self.marks = list(map(int,input().split()))
    def total(self):
        self.totalOfMarks = sum(self.marks)
        return self.totalOfMarks
    def avg(self):
        self.avgofMarks = sum(self.marks)/(len(self.marks))
        return self.avgofMarks
    def show(self):
        print("Total of Marks : ",self.totalOfMarks)
        print("Average of Marks : ",self.avgofMarks)


