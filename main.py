from bank_account import SavingAccount, CheckingAccount


s1 = SavingAccount("Scoobert Boinkus", 1000, 500, .10, 500)
s2 = SavingAccount("Alvin Tombunk", 1000, 500, .25, 501)
c1 = CheckingAccount("Dingle Klimberbob", 6000, 20, 50, 502)
c2 = CheckingAccount("Frodo Baggins", 50000, 5000, 1000, 503)

#Savings Account Testing
print("S1 Interest Deposit")
s1.print_customer_information()
accrued = s1.calc_interest(5)
s1.deposit(accrued)
s1.print_customer_information()

print("S2 Interest Deposit")
s1.print_customer_information()
accrued = s1.calc_interest(5)
s1.deposit(accrued)
s1.print_customer_information()

print("C1 Withdraw - PASS")
c1.print_customer_information()
c1.withdraw(49)
c1.print_customer_information()

print("C2 Withdraw - FAIL")
c2.print_customer_information()
c2.withdraw(1001)





