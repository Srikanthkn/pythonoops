class run:
    def get(self):
        self.rname=input("Enter runner Name")
        self.distance=int(input("Distance Covered"))
        return self.distance

    def show(self):
        print("Runnaer Name : ",self.rname)
        print("distance covered : ",self.distance)
