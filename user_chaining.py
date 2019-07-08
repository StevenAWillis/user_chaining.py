# Create a file with the User class, including the __init__ and make_deposit methods
#  Add a make_withdrawal method to the User class
#  Add a display_user_balance method to the User class
#  Create 3 instances of the User class
#  Have the first user make 3 deposits and 1 withdrawal and then display their balance
#  Have the second user make 2 deposits and 2 withdrawals and then display their balance
#  Have the third user make 1 deposits and 3 withdrawals and then display their balance
#  BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0.00
    def make_deposit(self, amount):
        self.account_balance += amount
        return self	
    
    def make_widthdrawal(self, amount):
        self.account_balance -= amount	
        return self
    def display_user_balance(self):
        print(f" User: {self.name}  , Balance: ${self.account_balance} ")
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount    
        return self

guido = User("Guido van Rossum", "guido@python.com")  
emmy = User("Emmy Tan", "emmy@python.com")
steebo = User("Steebo Steak", "stebo@python.com")

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_widthdrawal(100).display_user_balance()

emmy.make_deposit(200)
emmy.make_deposit(100)
emmy.make_widthdrawal(100)
emmy.make_widthdrawal(100)
emmy.display_user_balance()

steebo.make_deposit(1000)
steebo.make_widthdrawal(100)
steebo.make_widthdrawal(100)
steebo.display_user_balance()

guido.display_user_balance()
steebo.display_user_balance()
guido.transfer_money(steebo,40)
guido.display_user_balance()
steebo.display_user_balance()