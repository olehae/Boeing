class Bank:

    # initialize dictionary with names as keys and 0 as value
    def __init__(self, list_of_names):
        self.database = {name: 0 for name in list_of_names}

    # show current state of the dictionary
    def show(self):
        print("\n---Current Database---")
        for i in self.database:
            print(f"{i}: {self.database[i]}€")

    # add one or multiple users with the value 0
    def add_customer(self, customer):
        if type(customer) is str:
            self.database.update({customer: 0})
        elif type(customer) is list:
            for i in customer:
                self.database.update({i: 0})

    # delete one or multiple users from dictionary
    def remove_customer(self, customer):
        if type(customer) is str:
            del self.database[customer]
        elif type(customer) is list:
            for i in customer:
                del self.database[i]

    # add given amount to value of given key (name of customer)
    def deposit(self, key, amount):
        if amount < 0:
            print("\nCan´t deposit a negative amount")
        else:
            self.database[key] += amount

    # subtract given amount from value of given key
    def withdraw(self, key, amount):
        if amount < 0:
            print("\nCan´t withdraw a negative amount")
        elif self.database[key] < amount:
            print("\nCan´t withdraw, not enough money")
        else:
            self.database[key] -= amount


my_Bank = Bank(["Tom", "Tim", "Jack"])
my_Bank.show()
my_Bank.add_customer("Kevin")
my_Bank.show()
my_Bank.deposit("Kevin", 500)
my_Bank.show()
my_Bank.withdraw("Kevin", -1)
my_Bank.show()
my_Bank.deposit("Tim", -100)
my_Bank.add_customer(["Lisa", "Lena", "Lilly"])
my_Bank.show()
my_Bank.remove_customer("Tom")
my_Bank.remove_customer(["Lisa", "Lena"])
my_Bank.show()
