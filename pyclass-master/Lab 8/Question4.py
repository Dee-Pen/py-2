# create a loan program using setter and getter in class

class Loan:
    def __init__(self):
        self.principle = 0
        self.interest = 0
        self.time = 0

    def set_pamt(self,pamt):
        self.principle = pamt

    def set_int(self,rate):
        self.interest = rate

    def set_time(self,years):
        self.time = years

    def get_pamt(self):
        return self.principle
    
    def get_int(self):
        return self.interest
    
    def get_time(self):
        return self.time
    
    def calculate_interest(self):
        return (self.principle * self.interest * self.time) / 100
    
    def calculate_total(self):
        return self.principle + self.calculate_interest()
    
    def display(self):
        print("Principle amount: ",self.get_pamt())
        print("Interest rate: ",self.get_int())
        print("Time: ",self.get_time())
        print("Interest Amount: ",self.calculate_interest())
        print("Total amount: ",self.calculate_total())



pamount = int(input("Enter the principle amount: "))
irate = int(input("Enter the interest rate: "))
time = int(input("Enter the time in years: "))
l = Loan()
l.set_pamt(pamount)
l.set_int(irate)
l.set_time(time)
l.display()

