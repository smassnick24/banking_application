# banking_application

This is somewhat of my project statement / plan
For this project, I am going to create a banking system
(1) Define a BankAccount class that carries the necessary information for a bank account
    I would like for the object to store the individuals name, the account number, the routing number, and the balance.
    This class will have many public and private methods such as get_name, get_accountnumber, get_routingnumber etc.
(2) To scale this up, the information from each Account object will be stored in a SQLite3 database for validation purposes.
    For example, two accounts cant have the same routing or account number
(3) Then a GUI using Tkinter will be developed to implement a login/register system that have the functionalities to create a new account,
    Deposit and Withdraw funds, and transfer between accounts


APPLICATION FLOW:

While var_continue:
    
    login/register -> bool:
    if true:
        1) create account
        2) deposit
        3) withdraw
        4) display account
    else:
        input -> would you like to continue?
        if true:
            var_continue = true
        elif not true:
            var_continue = false