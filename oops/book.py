class book:
    def get(self):
        self.bookid = input("bookId : ")
        self.page = int(input("pages : "))
        self.price = int(input("price : "))
    def show(self):
        print("bookId",self.bookId)
        print("pages",self.pages)
        print("price",self.prices)
    def set(self,bId,pages,price):
        self.bookId = bId
        self.pages = pages
        self.prices = price
    def getPrice(self):
        if self.price > self.prices:
            return self.bookid,self.page,self.price
        else:
            return self.bookId,self.pages,self.prices

