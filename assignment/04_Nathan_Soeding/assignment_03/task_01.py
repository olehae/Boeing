cutomers = ["Alice", "Bob", "Chad"];
dic = {}


def create_dict(l):
    for c in l:
        dic[c] = 0


# Takes list of names that are added or removed
# If add is true customers will be added if it's false they will be removed
def change_customer(l, add):
    for c in l:
        if add:
          dic[c] = 0
        else:
            dic.pop(c)


def deposit(name, amount):
    if amount >= 0:
        dic[name] += amount
    else:
        print("Can't deposit negative amount")


def withdraw(name, amount):
    if 0 <= amount:
        if amount <= dic[name]:
            dic[name] -= amount
        else:
            print("Can't overdraw the account")
    else:
        print("Can't withdraw negative amount")


create_dict(cutomers)
print(dic)
change_customer(["Dave"], True)
print(dic)
change_customer(["Bob"], False)
print(dic)
deposit("Chad", 300)
print(dic)
withdraw("Chad", 30)
print(dic)
