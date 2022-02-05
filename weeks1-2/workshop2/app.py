from banking_pkg import account
import re


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# task 2
while True:
    name = input("Enter name to register: ")
# bonus tasks for pin and name
    if not re.match("^[a-z, A-Z]{1,10}$", name):
        print("Error! Only letters A-Z and 10 characters allowed!")
        continue
    pin = input("Enter PIN: ")
    if len(str(pin)) != 4:
        print("Must be a 4 digit pin.")
        continue
    else:
        balance = float(0)
        print(f"{name} has been registered with a starting balance of {balance}")
        break
# task 3
print("LOGIN")
while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
# task 5
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:
        account.logout(name)
        break
