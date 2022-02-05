def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("---------------------------------------------")
    print("| 1.    Login       | 2.    Register        |")
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donations  |")
    print("---------------------------------------------")
    print("|              5.    Exit                   |")
    print("---------------------------------------------")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation = username + " donated: $" + str(donation_amt)
    print("Thank you for your donation!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for idx in range(0, len(donations), 1):
            print(donations[idx])
