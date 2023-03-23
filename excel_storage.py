import pandas as pd
import os

class ExcelStorage:
    def __init__(self, filename):
        self.filename = filename

    def load_accounts(self):
        if os.path.exists(self.filename):
            df = pd.read_excel(self.filename, index_col=0)
            accounts = df.to_dict(orient='index')
            for username in accounts:
                accounts[username]['balance'] = int(accounts[username]['balance'])  # Convert balance to integer
            return accounts
        else:
            return {}

    def save_accounts(self, accounts):
        df = pd.DataFrame.from_dict(accounts, orient='index', columns=['password', 'balance'])
        df.index.name = 'username'
        df = df.reset_index()
        df['username'] = df['username'].astype(str)  # Ensure username is stored as a string
        df = df.set_index('username')
        df.to_excel(self.filename)

