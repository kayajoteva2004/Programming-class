# Treasure island game

print (" Welcome to the Treasure Island. "
       "\nYour mission is to find the treasure.\n"
       "\nYou're at a cross road. Where do you want to go?")
first = input("Type 'left' or 'right': ")



if first == 'left':
    second = input("\nYou reached a lake. There is an island in the middle of the lake.\n"
                    "Type 'wait' to wait for a boat. Type 'swim' to swim across: ")

    if second == 'wait':
        third = input("\nYou arrive at the island unharmed. There is a house with three doors - 'blue', 'yellow' and 'red'." 
                      "Which color do you choose? ")

        if third == 'yellow':
            print("\nYou Win!")
        elif third == 'red':
            print("\nThe room is full of fire. You die .Game Over.")
        elif third == 'blue':
            print("\nThe room is full of water. You drown. Game Over.")
    else:
            print("\n The lake is full of crocodiles who attacked you and you died. Game over.")
else:
    print("\nYou are attacked by a dragon. You die. Game over.")
