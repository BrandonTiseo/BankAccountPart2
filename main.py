from bank_account import SavingAccount, CheckingAccount


s1 = SavingAccount("Scoobert Boinkus", 90, 0, .10, 500)
c1 = CheckingAccount("Dingle Klimberbob", 6000, 20, 50, 501)

print("CheckingAccount Withdraw")
c1.print_customer_information()
print("WITHDRAWING")
c1.withdraw(5)
c1.print_customer_information()

print("CheckingAccount Withdraw FAIL")
c1.print_customer_information()
print("WITHDRAWING")
c1.withdraw(51)

print("SavingsAccount Interest Calculation")
s1.print_customer_information()
accrued = s1.calc_interest(4)
print("DEPOSITING")
print(f"I accrued ${accrued} in interest!")
s1.deposit(accrued)
s1.print_customer_information()

