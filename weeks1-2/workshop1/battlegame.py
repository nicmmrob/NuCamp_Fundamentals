# available characters to select with hp and damage
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
elf = "Elf"
elf_hp = 100
elf_damage = 100
human = "Human"
human_hp = 20
human_damage = 20
dragon_hp = 300
dragon_damage = 50

# step 1
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character:")
    if character == "1" or character == "Human":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
print("You have chosen the character:", character)
print("Health:", my_hp)
print("Damage:", my_damage)


# step 2
while True:
    dragon_hp -= my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle.")
        break
    my_hp -= dragon_damage
    print("The Dragon damaged the", character)
    print(f"The {character}'s hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break
