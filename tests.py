from bankaccount import BankAccount

savings = BankAccount("Samuel Massnick", 1, 1, "Savings", 0)

savings.deposit(111.11)
print(savings)

savings.deposit(float(50))
print(savings)

savings.deposit(50)
print(savings)