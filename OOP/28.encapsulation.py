class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        self.__balance-=amount
    #getter,setter
    def get_account_number(self):
        return self._account_number

    def get_account_balance(self):
        return self.__balance

if __name__ == '__main__':
    account = BankAccount("12345",1000)
    ac = account.get_account_number()
    print(ac)

    ab = account.get_account_balance()
    print(ab)