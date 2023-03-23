import pandas as pd
import os

class ExcelStorage:
    def __init__(self, filename):
        self.filename = filename

    def load_accounts(self):
        if os.path.exists(self.filename):
            df = pd.read_excel(self.filename, index_col=0)
            accounts = df.to_dict('index')
        else:
            accounts = {}
        return accounts

    def save_accounts(self, accounts):
        df = pd.DataFrame.from_dict(accounts, orient='index')
        df.to_excel(self.filename)
