from bankaccount import BankAccount
import sqlite3

conn = sqlite3.connect("bank_storage.db")
cur = conn.cursor()

def define_database():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT, account_number INTEGER, routing_number INTEGER, account_type TEXT, balance FLOAT)")
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT, password TEXT)")
    conn.commit()

def register_new_bankaccount(account: BankAccount):
    """Puts the given bank account into the accounts database"""
    if len(cur.execute(f"SELECT * FROM accounts WHERE account_number = {account.get_acnt()}").fetchall()) != 0:
        print("Account Number Taken")
        return False
    else:
        print("Account Registered")
        cur.execute(f"INSERT INTO accounts VALUES('{account.get_name()}', '{account.get_acnt()}', '{account.get_route()}', '{account.get_type()}', '{account.get_bal():.2f}')")
        conn.commit()
        return True
    
def update_balance(account: BankAccount):
    """updates the account balance of the given bank account in the database
       for example, if the user deposited or withdrew, this would be called afterward
       to update the database"""
    cur.execute(f"UPDATE accounts SET balance = {account.get_bal():.2f} WHERE account_number = {account.get_acnt()}")
    conn.commit()
    balance = list(cur.execute(f"SELECT * FROM accounts WHERE account_number = {account.get_acnt()}").fetchall())[0][4]  # grabbing the balance [0] for first account [4] for the balance index of the tuple
    return balance


def register_account(username, email, password):
    if len(cur.execute(f"SELECT * FROM users WHERE username = '{username}'").fetchall()) != 0:
        print("Username already taken")
        return False
    else:
        print("Account Registered")
        cur.execute(f"INSERT INTO users VALUES('{username}', '{email}', '{password}')")
        conn.commit()
        return True


def login(username, password):
    if cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"):
        print("Logged in successfully")
        print(cur.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'").fetchall())
        return True
    else:
        print("Username or Password Incorrect")
        return False






    
    
