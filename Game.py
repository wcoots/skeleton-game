import random

# Difficulty settings
dif = input("Select difficulty from 1 (easy) to 5 (hard)...")
while int(dif) < 1 or int(dif) > 5:
    dif = input("Select difficulty from 1 (easy) to 5 (hard)...")
print("\n")


# Player information
name = input("What is your name? ... ")
player = {"name": name, "health": 30, "experience": 0, "level": 1, "alive": True}  # ["key":value]
def print_player(player):
    for key, value in player.items():
        print(key, ":", value)
print("\n")


# Item choice
choice = 0
while choice == 0:
    item = input("Would you like a sword, a health potion, or neither? ...")
    print("\n")
    if item == str("sword") or item == str("s") or item == str("sw"):
        print("You took the sword! Attack's are now 2x more powerful")
        sword = 2
        choice = 1
    elif item == str("potion") or item == str("health") or item == str("health potion") or item == str("hp") or item == str("hp potion"):
        print("You took the potion! You now have 1.5x more health")
        player["health"] = player["health"] * 1.5
        sword = 1
        choice = 1
    elif item == str("neither") or item == str("none") or item == str("no"):
        print("You took nothing! Good luck!")
        sword = 1
        choice = 1
    elif item == str("both"):
        print("Don't be greedy!")
        choice = 0
    else:
        print("Unclear answer, please choose again")
        choice = 0


# Skeleton information and difficulty
z = 10 * int(dif)
skeleton = {"health": z, "alive": True}
def print_skeleton(skeleton):
    for key, value in skeleton.items():
        print(key, ":", value)


# Printing player info
input("")
print("YOUR STATS:")
print_player(player)
input("")


# Printing skeleton info
print("SKELETON'S STATS:")
print_skeleton(skeleton)
input("")


# The Fight
while skeleton["alive"] == True:
    if player["alive"] == True:

        # Skeleton's turn
        print("THE SKELETON ATTACKS!")
        input("")
        damageP = random.randrange(1, 51)
        exp = random.randrange((damageP - 10), damageP)
        if exp <= 0:  # Prevents negative exp
            exp = random.randrange(1, damageP)
        player["health"] = player["health"] - int(damageP/5)
        player["experience"] = (player["experience"] + int(exp))
        if float(player["experience"]/40) >= 1:
            player["level"] = player["level"] + 1  # After 40 exp is gained the player's level increases by 1
        player["experience"] = player["experience"] % 40  # After 40 exp is gained the player's exp returns to 0
        print(int(damageP/5), "damage taken")
        if player["health"] <= 0:
            player["health"] = 0  # Prevents negative hp
            print("Health remaining", player["health"])
            player["alive"] = False
            print("You died. RIP")
            input("")
            break
        print("Health remaining", player["health"])
        input("")
        print("Exp gained:", int(exp))
        print("Level:", player["level"])
        print("Exp to next level:", (40 - player["experience"]))

        input("")

        # Player's turn
        attack = input("ATTACK? (y/n) ...")
        print("\n")

        # Player attacks
        if attack == str("yes") or attack == str("y") or attack == str("ye"):
            damageS = random.randrange(1, 51) * float(sword)
            expS = random.randrange((damageS - 10), damageS)
            if expS <= 0:  # Prevents negative exp
                expS = random.randrange(1, damageS)
            skeleton["health"] = skeleton["health"] - int(damageS/5)
            player["experience"] = (player["experience"] + int(expS))
            if 2 > float(player["experience"] / 40) >= 1:
                player["level"] = player["level"] + 1  # After 40 exp is gained the player's level increases by 1
            elif float(player["experience"] / 40) >= 2:
                player["level"] = player["level"] + 1  # After 40 exp is gained the player's level increases by 1
            player["experience"] = player["experience"] % 40  # After 40 exp is gained the player's exp returns to 0
            print(int(damageS/5), "damage done")
            if skeleton["health"] < 0:
                skeleton["health"] = 0  # Prevents negative hp
            print("Skeleton's remaining health:", skeleton["health"])
            input("")
            print("Exp gained:", int(expS))
            print("Level:", player["level"])
            print("Exp to next level:", (40 - player["experience"]))
            if skeleton["health"] == 0:
                skeleton["alive"] = False
                print("You killed the skeleton. Well done!")
                input("")
                break
            input("")


        # Player doesn't attack
        elif attack == str("no") or attack == str("n") or attack == str("ne"):
            friendly = random.randrange(1, 5)

            # If skeleton is friendly
            if friendly == 1:
                print("You make friends with the skeleton. The end")
                input("")
                break

            # If skeleton isn't friendly
            else:
                print("The skeleton doesn't appear to be so kind")

        # If player didn't specify yes or no
        else:
            print("Unclear answer, miss your turn")
