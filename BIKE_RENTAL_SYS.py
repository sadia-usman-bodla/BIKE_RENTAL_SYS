class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def RentForBike(self,q):
        if q<=0:
            print("put greater than zero value")
        elif q>self.stock:
            print("enter the value less than stock")
        else:
            self.stock=self.stock-q
            print("total prices",q*100)
            print("total bikes",self.stock)
while True:
    obj=BikeShop(100)
    user_choice=int(input("""
                        1.display stock
                        2.rent a bike
                        3.exit    
                          """))
    if user_choice==1:
        obj.displayBike()
    elif user_choice==2:
        n=int(input("enter the quantity"))
        obj.RentForBike(n)
    else:
        break                            


