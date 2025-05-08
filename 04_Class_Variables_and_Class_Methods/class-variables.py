class Bank:
    bank_name = "Meezan Bank"  

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
       
    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")   


# Create an instance of the Bank class
account1 = Bank("Ali")
account2 = Bank("Kaneez Fatima")
account3 = Bank("M.Ubaid")

account1.display()
account2.display()
account3.display()

#Change the bank name using the class method
Bank.change_bank_name("Faysal Bank")
account1.display()
account2.display()
account3.display()
