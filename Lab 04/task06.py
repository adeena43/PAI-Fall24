class BankAccount:
    def __init__(self, acc_no, balance, date_of_opening, customer_name):
        self.acc_no = acc_no
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)

    def check_balance(self):
        print(f"Your account balance is: {self.balance}")


person1 = BankAccount("12345", 67000, "25-01-2004", "Adina Faraz")
person1.deposit(1000)
person1.withdraw(5000)
person1.check_balance()
