class Customer:
    def __init__(self, customer_name):
        self.name = customer_name
        self.money = 0

    def deposit(self, amount):
        if amount >= 0:
            self.money += amount
        else:
            print("Can't deposit negative amount")

    def withdraw(self, amount):
        if 0 <= amount:
            if amount <= self.money:
                self.money -= amount
            else:
                print("Can't overdraw the account")
        else:
            print("Can't withdraw negative amount")


class SavingsCustomer(Customer):
    def __init__(self, customer_name):
        Customer.__init__(self, customer_name)
        self.savings_balance = 0

    def move_to_savings(self, amount):
        if 0 <= amount:
            if amount <= self.money:
                self.money -= amount
                self.savings_balance += amount
            else:
                print("Can't overdraw the main balance")
        else:
            print("Can't move negative amount")

    def move_to_main(self, amount):
        if 0 <= amount:
            if amount <= self.savings_balance:
                self.savings_balance -= amount
                self.money += amount
            else:
                print("Can't overdraw the savings balance balance")
        else:
            print("Can't move negative amount")


alice = Customer("Alice")
bob = SavingsCustomer("Chad")
print(alice.name, alice.money)
print(bob.name, bob.money, bob.savings_balance)

alice.deposit(300)
print(alice.name, alice.money)
alice.withdraw(30)
print(alice.name, alice.money)

bob.deposit(300)
print(bob.name, bob.money, bob.savings_balance)
bob.move_to_savings(250)
print(bob.name, bob.money, bob.savings_balance)
bob.move_to_main(30)
print(bob.name, bob.money, bob.savings_balance)

