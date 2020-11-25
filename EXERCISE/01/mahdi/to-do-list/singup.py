from utility import Utility


class SingUp:
    @staticmethod
    def check_add(email, password):
        users = Utility.export_users()
        emails = users.keys()
        if Utility.email_type(email):
            if email in emails:
                print('That User already exist')
            else:
                if Utility.pass_type(password):
                    Utility.add_user(email, password)
                else:
                    print('Your Password is invalid !!')
        else:
            print('Email is incorrect!!!')
