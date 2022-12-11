class customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0


    def showbalance(self):
        print(f'This is the current balance of {self.name} : {self.balance}$.')
      

    def addbalance(self):
        valuetoadd = abs(int(input('Please state how much money you want to add to your account : ')))
        self.balance += valuetoadd
        print(f'Your account balance has been updated from {self.balance -valuetoadd}$ to {self.balance}$')


    def withdrawbalance(self, withdrawvalue = 0):
        if withdrawvalue == 0:
            withdrawvalue = abs(int(input('Please state how much money you would like to withdraw : ')))
        if withdrawvalue > self.balance:
            print('You cannot withdraw more money than your account contains.')
            return
        
        self.balance -= withdrawvalue
        print(f'Your account balance has been updated from {self.balance + withdrawvalue}$ to {self.balance}$')


class customersavings(customer):
    def __init__(self, name):
        self.savings = 0
        super().__init__(name)


    def addsavings(self):
        self.showbalance()
        valuetoadd = abs(int(input('Please state how much money you want to add to your savingsaccount : ')))

        if self.balance >= valuetoadd:
            self.savings += valuetoadd
            self.withdrawbalance(valuetoadd)
            print(f'Your savings account balance has been updated from {self.savings - valuetoadd}$ to {self.savings}$')

        else:
            print(f'Your can not add more to your savings than you posses.')
   
#if the manager has a list of customers he wants to create objects for he just uses a loop to iterate throught the list in order to create one object for each customer
#you could also put this thing into a loop and just add an option to change between customer accounts and use the object name as an identifiert 

customerone = customersavings('customerone')
print(customerone.savings)
customerone.showbalance()
customerone.addbalance()
customerone.addsavings()
