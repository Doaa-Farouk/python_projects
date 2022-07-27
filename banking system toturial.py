class User:
    def __init__(self, Name, Age, Gender):
        self.name = Name
        self.age = Age
        self.gender = Gender

    def show_details(self):
        print("Personal Details: ")
        print(f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}")


class Bank(User):
    # inheret from user class
    def __init__(self, Name, Age, Gender):
        super().__init__(Name, Age, Gender)
        # how much does the user have in his account
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        # how much does the user put in his account الوديعة
        self.balance += amount
        print(f"Account Balance Updated.")

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        # how much does the user take from his account
             # check whether user's balance is sufficient to withdraw
        if self.withdraw_amount > self.balance:
            print("You don't have this amount of money.")
            print(f"Amount of money in your account is only :{self.balance}")
        else:
            # withdraw the amount of money passed by the user from his balance
            self.balance -= self.withdraw_amount
            print(f"Account Balance Updated.")
        

    def view_balance(self):
        print(f"Amount of money in your account is : {self.balance}")
        pass


# create instances

# user_one = Bank("Omar", 30, "Male")
# user_two = Bank("Ola",29,"Female")

# running methods

# user_one.show_details()
# user_one.deposit(400)
# user_one.deposit(900)
# user_one.withdraw(2000)
# user_one.view_balance()

# user_two.view_balance()
