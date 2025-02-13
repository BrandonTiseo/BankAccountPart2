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

class SavingAccount(BankAccount):
    def __init__(self,customer_name, current_balance, minimum_balance, interest_rate):
        self.interest = interest_rate
        super().__init__(customer_name, current_balance, minimum_balance)

    #Calcultes your accrued interest for your current account balance over a certain amount of time in years.
    def calc_interest(self, years):
        accrued_interest = self.current_balance * self.interest * years
        return accrued_interest


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, withdraw_limit):

        #initialize parent
        super().__init__(customer_name, current_balance, minimum_balance)

        #store child parameters
        self.withdraw_limit = withdraw_limit

    def withdraw(self, withdraw_amount):

        if (withdraw_amount <= self.withdraw_limit):
            super().withdraw(withdraw_amount)
        else:
            print("Requested amount exceeds withdraw limit. Try again")




