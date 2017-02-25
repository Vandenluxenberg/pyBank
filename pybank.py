#!usr/bin/python

'''

Python Bank Account Manager (Code Academy Exercise)

Create accounts, then deposit and withdraw money from them.
Accounts are saved in a dictionary acting like a mini database.

TO DO :
- Save/load accounts database to/from a JSON file. Or an SQLite db ?
- Clear screen between each menu occurence (+ eventually remove sleep() calls)
- Add error handling for non numeric inputs during depost/withdraw

'''

from time import strftime, sleep

# Dictionary containing a database of all customers : { name : BankAccount instance }
bank_customers = {}

# Defines a class for every bank accounts
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

# Welcome message
def welcome():
    print "\nWelcome to Python Bank Account Manager."
    sleep(0.5)

# Menu to manage a single account (deposit, withdraw, etc)
def user_menu(name):
    while True:
        print "\n[ Manage account : %s ]" % name
        print "\nShow [B]alance, [S]how details, [D]eposit money, [W]ithdraw money, E[X]it."
        menu = raw_input("Your choice: ").upper()

        if menu == "B":  # Show balance
            bank_customers[name].show_balance()

        elif menu == "S":  # Show account details
            bank_customers[name].show_details()

        elif menu == "D":  # Deposit money
            amount = raw_input("Enter amount to deposit: ")
            bank_customers[name].deposit(amount)

        elif menu == "W":  # Withdraw money
            amount = raw_input("Enter amount to withdraw from account: ")
            bank_customers[name].withdraw(amount)

        elif menu == "X":  # Back to main menu
            break

        else:  # No valid command entered
            print "Error. Not a valid command."

# Main menu, manage accounts database (create, delete accounts,...)
def main_menu():
    while True:
        print "\n[C]reate account, [L]ist accounts, [M]anage account, [D]elete account, [Q]uit."
        menu = raw_input("Your choice: ").upper()

        if menu == "C":  # Create new bank account
            name = raw_input("Enter the account's holder name: ")
            if name in bank_customers:
                print "Error. An account with this name already exists."
            else:
                bank_customers[name] = BankAccount(name)
                sleep(0.8)
                print "New account for %s created." % name

        elif menu == "L":  # List all accounts in database by alphabetical order
            for name in sorted(bank_customers.keys()):
                sleep(0.1)
                print name

        elif menu == "M":  # Enter an account to manage it
            name = raw_input("Enter account name to manage: ")
            if name in bank_customers.keys():
                sleep(0.4)
                user_menu(name)
            else:
                print "Error. No account with this name."

        elif menu == "D":  # Delete an account
            name = raw_input("Enter account name to delete: ")
            if name in bank_customers.keys():
                del bank_customers[name]
                sleep(0.2)
                print "Account deleted."
            else:
                print "Error. No account with this name."

        elif menu == "Q":  # Quit the program
            print "\nGoodbye.\n"
            sleep(0.2)
            break

        else:  # No valid command entered
            print "Error. Not a valid command."

# Print the welcome message then Run the main program
welcome()

main_menu()

#EOF
