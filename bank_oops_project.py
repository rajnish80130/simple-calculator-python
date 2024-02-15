# bank opertion through oops

class Bank:
    bankname = 'Tsavvy Bank Of Bihar'
    branch = 'Patna,Bihar'

    # create account
    def __init__(self,username,pan,address):
        self.username = username
        self.pan = pan
        self.address = address
        self.balance = 0.0   #set ammount is to be 0.0
        print(f'Hello! {self.username} Congrats, Your Account Created Successfully...!')
    
    # deposit amount
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} Deposited Successfully...!")

    # Withdraw ammount
    def withdraw(self,withMoney):
        if withMoney > self.balance:
            print(f"You Can't WithDraw Money Because in your Balance Is {self.balance}")
        elif withMoney <= self.balance:
            self.balance = self.balance - withMoney
            print(f"{withMoney} Withdraw Successfully.")
    # Mini Statement
    def MiniStatement(self):
        print(f'Saving Money In Your Account is : {self.balance}')

print(f'Welcome to {Bank.bankname}.{Bank.branch}')
username = input("Enter Your Name : ")
Pan = input("Enter Your Pan Number : ")
Address = input("Enter Your Address : ")

b = Bank(username,Pan,Address)   #creating object of a bank class 

while True:
    Take_input = input("""
Please Select Any Option : 
1.Deposit
2.Withdraw
3.Ministatement
4.Exit
""")
    print(Take_input)

    if Take_input == '1':
        Amount = float(input("Enter Depoist Amount : "))
        b.deposit(Amount)

    elif Take_input == '2':
        withdraw_mon = float(input("Enter Money For Withdraw : "))
        b.withdraw(withdraw_mon)

    elif Take_input == '3':
        b.MiniStatement()

    elif Take_input == '4':
        print("Thanks For Using Our Banking Service....!")
        break
    
    else:
        print("invalid option")