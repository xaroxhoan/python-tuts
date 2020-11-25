from utility import Utility


class Login:
    @staticmethod
    def user_check(email, password):
        users = Utility.export_users()
        if email in users.keys():
            if password == users[email]:
                print('You are Logged in!!!')
            else:
                print('Your Password is incorrect!!!')
        elif email not in users.keys():
            print('Email is incorrect or You dont have account!!!')
