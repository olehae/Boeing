custs = ["tom", "bob", "tim", "jon"]
# 1
def bookmaking(names, balance = 0):
    customers = {}
    for i in names:
       customers[i] = balance
    return customers

customers = bookmaking(custs)

# 2
# to remove any amount of customers:
customers_to_remove = ["tim", "jon"]
for i in customers_to_remove:
    customers.pop(i)

# to add any amount of customers:
customers_to_add = ["mark", "bill"]
for i in customers_to_add:
    customers[i] = 0

# 3, 4
def deposit(name, amount):
    if amount >= 0:
        customers[name] = customers[name] + amount
        return customers
    else:
        print("invalid amount!")

def withdraw(name, amount):
    if customers[name] >= amount and amount >= 0:
        customers[name] = customers[name] - amount
        return customers
    else:
        print("invalid amount!")

# Test examples 
print(deposit("bob", 200))
print(withdraw("bob", 50))

