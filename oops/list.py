class lists:
    def fill(self):
          self.listOfI = list(map(int,input("Enter 5 Integer Values : ").split()))
    def max(self):
        self.maximumOfElement = max(self.listOfI)
    def min(self):
        self.minimumOfElement = min(self.listOfI)

    def display(self):
        print("Maximum of value : ",self.maximumOfElement)
        print("Minimum of value : ",self.minimumOfElement)