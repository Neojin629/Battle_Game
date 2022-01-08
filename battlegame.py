# Task 1 - Declaring game character variables

wizard = "Wizard"
elf = "Elf"
human = "Human"

# Declaring HP for each character

wizard_hp = 70
elf_hp = 100
human_hp = 150

# Declaring damage for each character

wizard_damage = 150
elf_damage = 100
human_damage = 20

# Declaring dragon HP and Damage

dragon_hp = 300
dragon_damage = 50

# Task 3 - Create the Infinite Loop

while True:

    # Task 2 - Prompt the player to choose from a list of options.

    print("1)    ", wizard)
    print("2)    ", elf)
    print("3)    ", human)

# Player selects character using input option.  Used int to change input from string to integer

    player_choice = int(input("Choose your character: "))

    # if statements to determine player_choice
    if player_choice == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        print("You have chosen ", wizard)
        print("Health: ", wizard_hp)
        print("Damage: ", wizard_damage)
        break
    if player_choice == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        print("You have chosen ", elf)
        print("Health: ", elf_hp)
        print("Damage: ", elf_damage)
        break
    if player_choice == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        print("You have chose ", human)
        print("Health: ", human_hp)
        print("Damage: ", human_damage)
        break
    else:
        print("Unknown Character")

        # Task 4 - Battle wih the Dragon, remember to set the variable to x = x-y

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at", character)
    print("The", character, "hitpoints are now:", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle.")
        break
