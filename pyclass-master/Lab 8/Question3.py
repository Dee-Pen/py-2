#calculate profit or loss on sp using class

class Product:
    def __init__(self,cp,sp):
        self.cp=cp
        self.sp=sp

    def netcost(self):
        if (self.sp>self.cp):
            print("Profit: ", self.sp - self.cp)
        elif(self.cp>self.sp):
            print("Loss: ", self.cp-self.sp)

cp = float(input("CP: "))
sp = float(input("SP: "))
obj = Product(cp,sp)
obj.netcost()