def login(database, username, password):
    if str(username) in database and database[username] == str(password):
        print("\n Welcome back,", username)
        return username
    elif str(username) in database and database[username] != str(password):
        print("\n Incorrect password for", username)
        return ""
    else:
        print("\n User not found. Please register")
        return ""


def register(database, username):
    if str(username) in database.keys():
        print("Username already registered.")
        return ""
    else:
        print("Your username has been registered.")
        return username

