import pandas as pd
from excel_storage import ExcelStorage


class BankApp:
    def __init__(self, excel_filename):
        self.storage = ExcelStorage(excel_filename)
        self.accounts = self.storage.load_accounts()
        self.current_account = None

    def save_accounts(self):
        self.storage.save_accounts(self.accounts)

    def create_account(self, username, password):
        if username in self.accounts:
            print("\nUsername already exists.")
        elif not password:  # Check if the password is empty
            print("\nPassword cannot be empty.")
        else:
            self.accounts[username] = {'password': password, 'balance': 1000}
            self.save_accounts()
            print("\nAccount created successfully.")

    def update_password(self, old_password, new_password):
        if self.current_account and self.accounts[self.current_account]['password'] == old_password:
            self.accounts[self.current_account]['password'] = new_password
            self.save_accounts()
            print("\nPassword updated successfully.")
        else:
            print("\nInvalid username or password.")

    def reload_accounts(self):
        self.accounts = self.storage.load_accounts()

    def login_account(self, username, password):
        self.reload_accounts() 
        if username in self.accounts and self.accounts[username]['password'] == password:
            self.current_account = username
            print("\nLogin successful.")
        else:
            print("\nInvalid username or password.")

    def view_balance(self):
        if self.current_account:
            balance = self.accounts[self.current_account]['balance']
            print(f"\nYour balance is: {balance}")
        else:
            print("\nYou are not logged in.")

    def send_money(self, to_username, amount):
        if self.current_account:
            if to_username in self.accounts:
                if self.accounts[self.current_account]['balance'] >= amount:
                    self.accounts[self.current_account]['balance'] -= amount
                    self.accounts[to_username]['balance'] += amount
                    self.save_accounts()
                    print("\nMoney sent successfully.")
                else:
                    print("\nInsufficient balance.")
            else:
                print("\nInvalid recipient.")
        else:
            print("\nYou are not logged in.")

    def deposit_money(self, amount):
        if self.current_account:
            if amount > 0:
                self.accounts[self.current_account]['balance'] += amount
                self.save_accounts()
                print(f"\n{amount} added to your account.")
            else:
                print("\nAmount should be greater than zero.")
        else:
            print("\nYou are not logged in.")

    def withdraw_money(self, amount):
        if self.current_account:
            if amount > 0 and self.accounts[self.current_account]['balance'] >= amount:
                self.accounts[self.current_account]['balance'] -= amount
                self.save_accounts()
                print(f"\n{amount} deducted from your account.")
            else:
                print("\nInsufficient balance or amount should be greater than zero.")
        else:
            print("\nYou are not logged in.")

    def logout(self):
        if self.current_account:
            self.current_account = None
            print("\nLogged out successfully.")
        else:
            print("\nYou are not logged in.")
