class Bank:
    def acntcre(self,acno,name,bank):
        self.acno=acno
        self.name=name
        self.bank=bank
        self.minb=5000
        self.balance=self.minb
    def credit(self,amnt):
        self.balance+=amnt
        print(" balance=",self.balance)
    def withdraw(self,amnt):
        if(amnt>self.balance):
            print("insufficient balance\navailable balance=",self.balance)
        else:
            self.balance-=amnt
            print("amnt debited\nbalance=",self.balance)

ob=Bank()
ob.acntcre(123,"mathews","sbi")
ob.credit(20000)
ob.withdraw(15000)