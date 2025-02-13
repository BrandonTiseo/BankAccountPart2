import bank_account


account_1 = bank_account.BankAccount("Brandon tiseo", 900, 100)
account_1.print_customer_information()

account_2 = bank_account.BankAccount("Andrew Tiseo", 90, 0)
account_2.print_customer_information()

#Testing invalid withdraw
print("WITHDRAWING")
account_1.withdraw(801)
account_1.print_customer_information()

#Testing proper withdraw
print("WITHDRAWING")
account_1.withdraw(50)
account_1.print_customer_information()

print("DEPOSITING")
account_1.deposit(1000)
account_1.print_customer_information()

#Bank Account Part 2 Testing Code
saving_account = bank_account.SavingAccount("Scoobert Boinkus", 90, 0, .05)
accrued = saving_account.calc_interest(4)
print(f"I accrued ${accrued} in interest!")