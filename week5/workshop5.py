import random


def guess_random_number(tries, start, stop):
    random_number = random.randrange(start, stop)
    while tries != 0:
        print("You have", tries, "remaining.")
        user_guess = input("Guess the number: ")
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("That's an awesome guess! Spot on.")
            return
        elif user_guess < random_number:
            print("Guess higher!")
        else:
            print("Guess lower!")
        tries -= 1
    print("Sorry, you've run out of attempts.")

# driver code for task 1
#guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    random_number = random.randrange(start, stop)

    while tries != 0:
        linear_guess = start
        print("The number for the program to guess is:", random_number)
        print("Number of tries left:", tries)
        print("The computer is guessing...", linear_guess)
        if linear_guess == random_number:
            print("The program has guessed correctly.")
            return
        else:
            linear_guess += 1
        tries -= 1
    print("The program has failed to guess the correct number.")


# driver code for task 2
#guess_random_num_linear(5, 0, 10)

def guess_random_num_binary(tries, start, stop):
    random_number = random.randrange(start, stop)

    # while tries != 0:
    print("The number for the program to guess is:", random_number)
    print("Number of tries left:", tries)

    low = start
    high = stop - 1
    mid = (start + stop) // 2

    linear_guess = mid
    while low <= high:
        if linear_guess < random_number:
            low = linear_guess + 1
            tries -= 1
            print("Guessing higher!")
        elif linear_guess > random_number:
            print("Guessing lower!")
            low = linear_guess - 1
            tries -= 1
        else:
            return linear_guess
        print("The computer is guessing...", linear_guess)
        return -1


# driver code for task 3
guess_random_num_binary(5, 0, 100)
