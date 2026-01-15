class BankAccount:
    def __init__(self,number):
        if len(str(number)) == 26:
            self.number = str(number)
            self.balance = 0
        else:
            return 'Error. Bank account number must be 26 digits.'
        
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            return print('Insufficient funds on the account')
        else:
            self.balance -= amount

    def display(self):
        print(f'Bank Account No: {self.number[0:2]} {self.number[2:6]} {self.number[6:10]} {self.number[10:14]} {self.number[14:18]} {self.number[18:22]} {self.number[22:26]}')
        print(f'Balance: PLN {self.balance}')

def main():
    account_1 = BankAccount(12345655559090111100007722)
    account_1.display()
    account_1.deposit(25.30)
    account_1.display()
    account_1.withdraw(31.70)
    account_1.display()
    account_1.withdraw(14)
    account_1.display()

if __name__ == '__main__':
    main()