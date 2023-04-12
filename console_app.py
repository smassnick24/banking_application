from database_work import register_new_bankaccount, update_balance, register_account, login
from bankaccount import BankAccount

var_continue = True


print("Welcome to Sam's Banking Application")
while var_continue:
    print("What would you like to do?")
    print("1) Login")
    print("2) Registration")
    print("3) Quit")
    user = input()
    if user == '1' or user.lower() == 'login':
        print("Logging in...")
        username = input("Username: ")
        password = input("Password (Case Sensitive): ")
        login(username.lower(), password)
        print("What you like to do now?")
        print("1) Register New Bank Account")
        print("2) ")
    if user == '2' or user.lower() == 'register':
        print("Registering...")
        username = input("Username: ")
        password = input("Password (Case Sensitive): ")
        register_account(username, password)
    if user == '3' or user.lower() == 'quit':
        print("Have a nice day!")
        break
    
    