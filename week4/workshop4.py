class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        return name

    def change_pin(self, pin):
        self.pin = pin
        return pin

    def change_password(self, password):
        self.password = password
        return password
# this above function/method are given to each instance of this class. Each instance can change_name, change_pin, and change_password.


class BankUser(User):
    def __init__(self, name, pin, password):
        # called on the super function to get all the attributes from parent class.
        super().__init__(name, pin, password)
        self.balance = 0

    # this is a function/method a user can call on to show balance.
    def show_balance(self, balance):
        print(f"{self.name} has an account balance of: ${balance}")

    # this is a function/method a user can call on to withdraw money from the user's account.
    def withdraw(self):
        wbalance = input("How much would you like to withdraw? ")
        self.balance -= float(wbalance)
        print(f"{self.name} has an account balance of: ${self.balance}")

    # this is a function/method a user can call on to deposit money into the user's account.
    def deposit(self):
        dbalance = input("How much would you like to deposit? ")
        self.balance += float(dbalance)
        print(f"{self.name} has an account balance of: ${self.balance}")

    # this is a function/method a user can call on to transfer money to another user's account.
    def transfer_money(self, user, amt):
        print("\nAuthentication required...")
        w_pin = input("Please enter your pin: ")
        if w_pin != self.pin:
            print("Invalid credentials. Transaction cancelled.")
            print(f"{self.name} has a balance of: ${self.balance}")
        else:
            print(f"You are transferring ${amt} to {user.name}")
            if amt <= self.balance:
                self.balance -= float(amt)
                user.balance += float(amt)
                print(f"{self.name} has a balance of: ${self.balance}")
                print(f"{user.name} has a balance of: ${user.balance}")
            else:
                print("Insufficient funds.")

    # this is a function/method a user can call on to request money from another user's account.
    def request_money(self, user, amt):
        print("\nUser authentication is required...")
        u_pin = input(f"Enter {user.name}'s pin: ")
        y_pw = input(f"Enter your password: ")
        if u_pin != user.pin and y_pw != self.password:
            print("Invalid credentials. Transaction cancelled.")
            print(f"{self.name} has a balance of: ${self.balance}")
        else:
            print(f"You are requesting ${amt} from {user.name}")
            if amt <= user.balance:
                self.balance += float(amt)
                user.balance -= (amt)
                print(f"{self.name} has a balance of: ${self.balance}")
                print(f"{user.name} has a balance of: ${user.balance}")
            else:
                print("Insufficient funds.")


""" Driver Code for Task 1 """
# ob1 = User("Bob", 1234, "password")
# print(ob1.name, ob1.pin, ob1.password)

""" Driver Code for Task 2 """
# ob2 = User("Bob", 1234, "password")
# print(ob2.name, ob2.pin, ob2.password)
# print(ob2.change_name("Bobby"), ob2.change_pin(
#     4321), ob2.change_password("newpassword"))

""" Driver Code for Task 3 """
# ob3 = BankUser("Bob", 1234, "password")
# print(ob3.name, ob3.pin, ob3.password, ob3.balance)

""" Driver Code for Task 4 """
# ob4 = BankUser("Bob", 1234, "password")
# ob4.show_balance(ob4.balance)
# ob4.deposit()
# ob4.withdraw()

""" Driver Code for Task 5"""
user1 = BankUser("Bob", "1234", "password")
user2 = BankUser("Alice", "4321", "diffpw")
user2.balance = 5000
user2.show_balance(user2.balance)
user1.show_balance(user1.balance)

user2.transfer_money(user1, 50)
user1.request_money(user2, 1000)
user2.request_money(user1, 50)
user1.transfer_money(user2, 50)
