class Customer:
    # initialize attributes
    def __init__(self, name):
        self.name = name
        self.balance = 0

    # show current balance (of main account)
    def show(self):
        print(f"Balance of {self.name}: {self.balance}")

    # add given amount to balance (of main account)
    def deposit(self, amount):
        if amount < 0:
            print("\nCan´t deposit a negative amount")
        else:
            self.balance += amount

    # subtract given amount from balance (of main account)
    def withdraw(self, amount):
        if amount < 0:
            print("\nCan´t withdraw a negative amount")
        elif self.balance < amount:
            print("\nCan´t withdraw, not enough money")
        else:
            self.balance -= amount


# create child class from Customer class
class SavingsCustomer(Customer):
    def __init__(self, name):
        # inherit name from parent class
        super().__init__(name)
        # initialize new attribute for child
        self.savings_balance = 0

    # add given amount to savings balance and subtract it from main balance
    def deposit_to_savings(self, amount):
        if amount > self.balance:
            print("\nCan´t deposit, not enough money in your account")
        else:
            self.savings_balance += amount
            self.balance -= amount

    # subtract given amount from savings account and add it to main balance
    def withdraw_from_savings(self, amount):
        if amount < 0:
            print("\nCan´t withdraw a negative amount")
        elif self.savings_balance < amount:
            print("\nCan´t withdraw, not enough money")
        else:
            self.savings_balance -= amount
            self.balance += amount

    # show current savings balance
    def show_savings(self):
        print(f"Savings balance of {self.name}: {self.savings_balance}")


customer1 = SavingsCustomer("Tim")
customer1.show()
customer1.deposit(500)
customer1.show()
customer1.show_savings()
customer1.deposit_to_savings(200)
customer1.show()
customer1.show_savings()
customer1.withdraw_from_savings(201)
