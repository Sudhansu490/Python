class Bank:
    bankname="State Bank of India"
    branch="A23,BBSR,India,751012"

    # create account
    def __init__(self):
        print(f'Welcome to {Bank.bankname},{Bank.branch}')
        self.username= input('Enter Your Name:')
        self.age= int(input('Enter Your Age:'))
        self.gender= input('Enter Your Gender(Male/Female/Transgender):')
        self.pan= input('Enter Your PAN ID:')
        self.address= input('Enter Your Address:')
        self.balance= 0.0  # set account balance to 0.0
        print(f'Hello {self.username}, Congrats! Your account Created Sucessfully.')

    # Deposit
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount} deposited successfully.')

    # Withdraw
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully.Remaining Balance is {self.balance}')
        else:
            print('Insufficient Funds.')

    # Check Balance
    def checkBalance(self):
        print(f'Your Account balance is {self.balance}')
        
b=Bank()

while True:
    option=int(input('\nSelect Any Option: \n1.Deposit \n2.Withdraw \n3.Check Balance \n4.Stop \n'))
    if option==1:
        amount=float(input('Enter Deposited Amount:'))
        b.deposit(amount)
    elif option==2:
        amount=float(input('Enter Withdraw Amount:'))
        b.withdraw(amount)
    elif option==3:
        b.checkBalance()
    elif option==4:
        print('Thanks for using State Bank of India...')
        break
    else:
        print('Invalid Option,Plz select a valid option.')