class emp:
    def empDetails(self):
        self.empNumber = int(input("Employee Number : "))
        self.empComp = float(input("employee Compensation : "))
    def display(self):
        print()
        print(".....Employee Deataild........")
        print("EmpNumber : ",self.empNumber)
        print("EmpCompensation : ",self.empComp)
