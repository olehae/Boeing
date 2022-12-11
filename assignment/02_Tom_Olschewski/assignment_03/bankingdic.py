def createdict(customers):
    bankingdict = {customer : 0 for customer in customers}
    return bankingdict


def showbalance(bankingdict, customerid):
    print(f'This is the current balance of {customerid} : {bankingdict[customerid]}$.')


def addbalance(bankingdict, customerid):
    valuetoadd = abs(int(input('Please state how much money you want to add to your account : ')))
    bankingdict.update({customerid: bankingdict[customerid] + valuetoadd})
    print(f'Your account balance has been updated from {bankingdict[customerid]-valuetoadd}$ to {bankingdict[customerid]}$')


def withdrawbalance(bankingdict, customerid):
    withdrawvalue = abs(int(input('Please state how much money you would like to withdraw : ')))
    if withdrawvalue > bankingdict[customerid]:
        print('You cannot withdraw more money than your account contains.')
        
    bankingdict.update({customerid: bankingdict[customerid] - withdrawvalue})
    print(f'Your account balance has been updated from {bankingdict[customerid]+withdrawvalue}$ to {bankingdict[customerid]}$')


customers = ['customerone', 'customertwo', 'customerthree']
#could easily add a loop here where i show the manager the current dictionary with all is customers where he may add and remove customer accounts by typing in their dic key (name)
#which either adds that key with start value of 0 (if key doesnt already exitst) or it removes the key from the dic
bankingdict = createdict(customers)
print(bankingdict, type(bankingdict))
print('Welcome, this is Schewkisbank!')

while True:
    #could also put this in a seperate loop and add a home menu where you can change between customers without restarting the programm, but 2 lazy.
    #Functionality is shown I thinks thats sufficient.
    customerid = input('Please enter your customerid : ')
    if customerid not in customers:
        print('Invalid customerid, please try again! \n')
        continue

    else:
        break

while True:
    courseofaction = int(input('Press 1 to view your holdings, press 2 to add balance to your account, press 3 to withdraw money, press 4 to quit : '))

    if courseofaction == 1:
        showbalance(bankingdict, customerid)

    elif courseofaction == 2:
        addbalance(bankingdict, customerid)

    elif courseofaction == 3:
        withdrawbalance(bankingdict, customerid)

    elif courseofaction == 4:
        print('Have a great day!')
        break

    else:
        print("The number you entered was invalid, try again. \n")