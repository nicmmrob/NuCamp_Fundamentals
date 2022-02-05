from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""
show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")
else:
    print("Logged in as:", authorized_user)

while True:
    user_choice = input("\nChoose an option: ")
    if user_choice == "1":  # option 1
        username = input("\nWhat is your username? ")
        password = str(input("What is your password? "))
        authorized_user = login(database, username, password)
    elif user_choice == "2":  # option 2
        username = input("\nCreate your username: ")
        password = input("Create a password: ")
        authorized_user = register(database, username)
        if str(authorized_user) != "":
            database[username] = password
    elif user_choice == "3":  # option 3
        if str(authorized_user) == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif user_choice == "4":  # option 4
        show_donations(donations)
    elif user_choice == "5":
        print("Goodbye.")
        break
    else:  # invalid option
        print("Not a valid option")

    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
