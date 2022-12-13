
class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

# 2. / 3.
    def deposit(self, amountplus):
        self.amountplus = amountplus
        if amountplus >= 0: 
            self.balance += self.amountplus
        else:
            print("Amount cannot be transfered!")

    def withdraw(self, amountminus):
        self.amountminus = amountminus
        if amountminus >= 0 and self.balance > amountminus:
            self.balance -= self.amountminus
        else:
            print("Amount cannot be transfered!")
            


# 4. 
class SavingsCustomer(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.savings = 0
    
    def transfer_to_savings(self, amount):
        self.amount = amount
        if amount > 0 and self.balance > amount:
            self.savings += self.amount 
            self.balance -= self.amount
        else:
            print("Amount cannot be transfered!")

    def transfer_from_savings(self, amount):
        self.amount = amount
        if amount > 0 and self.savings > amount:
            self.savings -= self.amount
            self.balance += self.amount
        else:
            print("Amount cannot be transfered!")


# Test examples
bob = Customer("bob")
bob.deposit(600)
print(bob.name, " has" ,bob.balance, " euros in his bank account")
bob.withdraw(150)
print(bob.name, " has" ,bob.balance, " euros in his bank account")
jon = SavingsCustomer("jon")        
jon.deposit(400)
print(jon.name, " has" ,jon.balance, " euros in his bank account")
jon.transfer_to_savings(130)
print(jon.name, " has" ,jon.balance, " euros in his bank account")
print(jon.name, " has" ,jon.savings, " euros in his savings account")
jon.transfer_from_savings(150)
print(jon.name, " has" ,jon.balance, " euros in his bank account")
print(jon.name, " has" ,jon.savings, " euros in his savings account")
jon.transfer_from_savings(85)
print(jon.name, " has" ,jon.balance, " euros in his bank account")
print(jon.name, " has" ,jon.savings, " euros in his savings account")

