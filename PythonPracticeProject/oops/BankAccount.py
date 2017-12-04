class BankAccount:
    def __init__(self, name, money):
        self.__name=name
        self.__balance = money #__balance is private now, so it is only accessable inside the class
        
    def deposite(self, money):
        self.__balance+=money
    def withdraw(self, money):
        if self.__balance>money:
            self.__balance-=money
            return money
        else:
            return "insufficient funds"
        
    def checkbalance(self):
        return self.__balance
    
b1 = BankAccount("SadaLearningHub",500)
print("WithDraw the money : ", b1.withdraw(600))
b1.deposite(500)
print("Checking balance : ", b1.checkbalance())
print("WithDraw the money : ", b1.withdraw(600))
print("Checking balance : ", b1.checkbalance())
