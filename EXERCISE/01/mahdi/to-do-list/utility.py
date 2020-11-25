import re
import pandas as pd


class Utility:

    @staticmethod
    def email_type(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        result = re.search(regex, email)
        if result:
            return 1
        else:
            return 0

    @staticmethod
    def pass_type(password):
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if mat:
            return 1
        else:
            return 0

    @staticmethod
    def add_user(email, password):
        df = pd.read_excel('./DataBase.xlsx', 0)
        df = df.append({'email': email, 'password': password}, ignore_index=True)
        df.to_excel('./DataBase.xlsx', 'users', index=False)

    @staticmethod
    def export_users():
        df = pd.read_excel('./DataBase.xlsx', 0)
        users = {}
        for index, (email_db, password_db) in df.iterrows():
            users.update({email_db: password_db})
        return users
