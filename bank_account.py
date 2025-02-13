class BankAccount:
    bank_title = "Banking Bank"

    def __init__(self,customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if(self.current_balance <= self.minimum_balance or (self.current_balance - withdraw_amount) < self.minimum_balance):
            print("Balance is below the minimum balance, cannot withdraw.")
        else:
            self.current_balance -= withdraw_amount

    def print_customer_information(self):
        print(f"{self.bank_title} Customer Info \nName: {self.customer_name}\nCurrent Balance: {self.current_balance}\nMinimum Balance: {self.minimum_balance}\n")



#main program
account_1 = BankAccount("Brandon tiseo", 900, 100)
account_1.print_customer_information()

account_2 = BankAccount("Andrew Tiseo", 90, 0)
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

