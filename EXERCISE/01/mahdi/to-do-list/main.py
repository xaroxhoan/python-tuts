from singup import SingUp
from login import Login


x = input('Please login if you have an account.if you dont have create a new ..chose 1 for login & 2 for sing up: ')
if x == '1':
    email = input('input your email address:  ')
    password = input('please input your password:  ')
    Login.user_check(email, password)
elif x == '2':
    email = input('input your email address:  ')
    password = input('please input your password:  ')
    SingUp.check_add(email, password)
