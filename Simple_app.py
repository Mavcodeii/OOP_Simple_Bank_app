class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, 'has an account balance of:',
              str(f'{self.balance: .2f}'))

    def widthdraw(self, w_amount):
        self.balance = self.balance - float(w_amount)
        return

    def deposit(self, d_amount):
        self.balance = self.balance + float(d_amount)
        return

    def transfer_money(self, transfer_user):
        transfer_amount = 500       # Could add an input to request the amount
        print('You are transferring ' + '$' +
              str(transfer_amount) + ' to ' + transfer_user.name)
        print('Authentication required')
        auth_pin = input('Enter your PIN: ')
        if auth_pin == str(self.pin):
            print('Transfer authorized')
            print('Transferring ' + '$' +
                  str(transfer_amount) + ' to ' + transfer_user.name)
            self.widthdraw(transfer_amount)
            transfer_user.deposit(transfer_amount)
            return True
        else:
            print('Invalid PIN. Transaction canceled.')
            return False

    def request_money(self, request_user):
        request_amount = 250
        print('You are requesting ' + '$' +
              str(request_amount) + ' from ' + request_user.name)
        print('User authentication is required...')
        auth_pin = input('Enter ' + request_user.name + ' PIN:')
        if auth_pin == str(request_user.pin):
            auth_password = input('Enter your password: ')
            if auth_password == self.password:
                print('Request authorized')
                print(request_user.name + ' sent ' + '$' + str(request_amount))
                request_user.widthdraw(request_amount)
                self.deposit(request_amount)
                return
            else:
                print('Invalid password. Transcation canceled.')
        else:
            print('Invalid PIN. Transaction canceled.')


drive_code5a = BankUser('Bob', 1234, 'password')
drive_code5b = BankUser('Alice', 4567, 'code')

drive_code5b.deposit(5000)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()
drive_code5b.transfer_money(drive_code5a)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()
drive_code5b.request_money(drive_code5a)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()


""" 
--------------Driver Code for  Task 1--------------

drive_code1 = User('Bob', 1234, 'password')
print(drive_code1.name, drive_code1.pin, drive_code1.password)

"""


""" 
--------------Driver Code for  Task 2--------------


drive_code2 = User('Bob', 1234, 'password')
print(drive_code2.name, drive_code2.pin, drive_code2.password)
drive_code2.change_name('Mark')
drive_code2.change_pin(4567)
drive_code2.change_password('testpassword')
print(drive_code2.name, drive_code2.pin, drive_code2.password)

"""

""" 
--------------Driver Code for  Task 3--------------


drive_code3 = BankUser('Bob', 1234, 'password')
print(drive_code3.name, drive_code3.pin,
      drive_code3.password, drive_code3.balance)
"""

""" 
--------------Driver Code for  Task 4--------------


drive_code4 = BankUser('Bob', 1234, 'password')

drive_code4.show_balance()
drive_code4.deposit(1000)
drive_code4.show_balance()
drive_code4.widthdraw(500)
drive_code4.show_balance()
"""

""" 
--------------Driver Code for  Task 5--------------

drive_code5a = BankUser('Bob', 1234, 'password')
drive_code5b = BankUser('Alice', 4567, 'code')

drive_code5b.deposit(5000)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()
drive_code5b.transfer_money(drive_code5a)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()
drive_code5b.request_money(drive_code5a)
drive_code5b.show_balance()
drive_code5a.show_balance()
print()

"""
