import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    choice = input("Hit Enter to draw a card or press Q+Enter to quit: ")
    # short-hand for giving the user more variety so as not be tied to the shift key
    if choice in ("Q", "q"):
        break
    # drawing a random item from the list of diamonds
    new_card = random.choice(diamonds)
    # removing the card that was drawn from the list of diamonds
    diamonds.remove(new_card)
    print(f"The deck now constists of: {diamonds}.")
    hand.append(new_card)  # adding the card that was drawn to the hand
    print(f"You currently have {hand} in your hand.")
# this will quit once there are no more cards to draw.
if not diamonds:
    print("There are no more cards to pick.")
