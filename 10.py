class ATM:
    def _init_(self):
        self.balance=0
    def deposit(self):
        amount=int(input("!!Enter the deposit amount!!\n"))
        self.balance=amount
        print("Toatal Balance is:",self.balance)
    def withdraw(self):
        amount=int(input("!!Enter the withdraw amount!!\n"))
        if(amount>self.balance):
            print("Insufficiant balance")
        else:
            self.balance=self.balance-amount
            print("Remaining Balance is:",self.balance)
    def balanceEnquairy(self):
        print("!!Balance Enquairy!!")
        print("The balance is:",self.balance)

a=ATM()
a.deposit()
a.withdraw()
a.balanceEnquairy()
