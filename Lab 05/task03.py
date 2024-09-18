class Account:
    def __init__(self):
        self.__account_no = "0"
        self.__account_bal = 0
        self.__security_code = ""

    def initialize(self, number, balance, code):
        self.__account_no = number
        self.__account_bal = balance
        self.__security_code = code

    def print(self):
        print(f"Account number: {self.__account_no}")
        print(f"Account balance: {self.__account_bal}")
        print(f"Account code: {self.__security_code}")

acc1 = Account()
acc1.initialize("4134567890", 6700, "AdinaFar_31")
acc1.print()
