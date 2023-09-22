class tollbooth:
    def __init__(self):
        self.Noofcars=0
        self.amount=0
    def payingcar(self,a):
        self.amount +=a
        self.Noofcars +=1
    def nopaying(self,a):
       self.amount +=a
       self.Noofcars+=1
    def display(self):

        print("amount",self.amount)
        print("noofcars",self.Noofcars)
