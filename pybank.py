#!usr/bin/python

'''
Python Bank Account Manager (Code Academy Exercise)
'''

from time import strftime, sleep

class BankAccount(object):
    balance = 0
    date_created = ""

    def __init__(self, name):
        self.name = name
        self.date_created = strftime("%B %d, %Y")

    def __repr__(self):
        return "%s's Account. Balance: $%.2f." % (self.name, self.balance)

    def show_balance(self):
        sleep(0.1)
        print "Account balance: $%.2f." % self.balance

    def show_details(self):
        sleep(0.1)
        print "Account's holder: %s. Account created on %s. Balance: $%.2f." % (self.name, self.date_created, self.balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            print "Amount must be positive!"
        else:
            self.balance += amount
            sleep(0.2)
            print "Done.",
            self.show_balance()

    def withdraw(self, amount):
        amount = float(amount)
        if ( self.balance - amount <= 0 ):
            q = raw_input("Your balance will be negative! Continue (Y/N)? ").upper()
            if q != "Y":
                return
        self.balance -= amount
        sleep(0.2)
        print "Done.",
        self.show_balance()

def welcome():
    print "\nWelcome to Python Bank Account Manager."
    sleep(0.5)

def main_menu():
    while True:
        print "\n[C]reate account, Print [B]alance, [P]rint details, [D]eposit money, [W]ithdraw money, [Q]uit."
        menu = raw_input("Your choice: ").upper()

        if menu == "C":
            name = raw_input("Enter the account's holder name: ")
            print "Creating new account..."
            account = BankAccount(name)
            sleep(1)
            print "New account for %s created." % name

        elif menu == "B":
            account.show_balance()

        elif menu == "P":
            account.show_details()

        elif menu == "D":
            amount = raw_input("Enter amount to deposit: ")
            account.deposit(amount)

        elif menu == "W":
            amount = raw_input("Enter amount to withdraw from account: ")
            account.withdraw(amount)

        elif menu == "Q":
            print "\nGoodbye.\n"
            sleep(0.2)
            break

        else:
            print "Error. Not a valid command."

welcome()

main_menu()

#EOF
