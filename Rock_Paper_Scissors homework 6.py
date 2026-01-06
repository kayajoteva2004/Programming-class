import random

print("I want to play rock_paper_scissors!")
print("Select 0 for rock, 1 for paper and 2 for scissors.")

# Emojis
game_board = ["✂️", "📃", "🪨"]

your_choice = int(input("Your choice: "))
print("Your choice:", game_board[your_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:", computer_choice)
print(game_board[computer_choice])

if your_choice == computer_choice:
    print("It's a draw!")
elif ((your_choice == 0 and computer_choice == 2) or
      (your_choice == 1 and computer_choice == 0) or
      (your_choice == 2 and computer_choice == 1)):
    print("You win!")
else:
    print("You lose!")
