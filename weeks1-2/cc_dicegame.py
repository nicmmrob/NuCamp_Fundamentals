import random

high_score = 0


def dice_game(high_score):
    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "2" or choice == "Leave Game":
            print("Goodbye!")
            break
        if choice == "1" or choice == "Roll Dice":
            print("\nYou roll 2d6\n")
            dice_roll_1 = random.randint(1, 6)
            print("You rolled a:", dice_roll_1)
            dice_roll_2 = random.randint(1, 6)
            print(f"You rolled a: {dice_roll_2} \n")
            dice_roll_total = dice_roll_1 + dice_roll_2
            print(f"You have rolled a total of: {dice_roll_total} \n")
        if dice_roll_total > high_score:
            print("New high score!\n")
            new_high_score = dice_roll_total
            return dice_game(new_high_score)
        else:
            return dice_game(high_score)


dice_game(high_score)
