class BankAccount:
    def __init__(self):
        self.__balance = 0

    # пополнение баланса карты
    def deposit(self, amount):
        self.__balance += amount

    # снятие денег с карты
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Недостаточно средств')

    def display_balance(self):
        print('Ваш баланс: ', self.__balance)


account = BankAccount()
account.display_balance()
account.deposit(100000)
account.display_balance()
account.withdraw(700)
account.display_balance()
