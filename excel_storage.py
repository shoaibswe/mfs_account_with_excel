import pandas as pd
import os

class ExcelStorage:
    def __init__(self, filename):
        self.filename = filename

    def load_accounts(self):
        if os.path.exists(self.filename):
            df = pd.read_excel(self.filename, index_col=0, dtype={'password': str})  # Ensure password is read as a string
            accounts = df.to_dict(orient='index')
            for username in accounts:
                accounts[username]['balance'] = int(accounts[username]['balance'])
            return accounts
        else:
            return {}

    def save_accounts(self, accounts):
        df = pd.DataFrame.from_dict(accounts, orient='index', columns=['password', 'balance'])
        df.index.name = 'username'
        df = df.reset_index()
        df['username'] = df['username'].astype(str)
        df['password'] = df['password'].astype(str)  # Ensure password is stored as a string
        df = df.set_index('username')
        df.to_excel(self.filename, index=True)
