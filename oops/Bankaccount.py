class bankaccount:
    def __init__(self):
        self.nameOfAccountHolder = " "
        self.accountNumber = "0000****"
        self.typeOfAccount = "savings"
        self.balanceamount = 0
    def createAccount(self,name  , acno , type , bal):
        self.nameOfAccountHolder = name
        self.accountNumber = acno
        self.typeOfAccount = type
        self.balanceamount =bal
    def deposit(self,dep):
        self.balanceamount =self.balanceamount + dep
    def withdraw(self,wit):
        self.balanceamount= self.balanceamount - wit

    def display(self):
        print(self.nameOfAccountHolder)
        print(self.accountNumber)
        print(self.typeOfAccount)
        print(self.balanceamount)

