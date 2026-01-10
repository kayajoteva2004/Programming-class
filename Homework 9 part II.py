import random

words = ["muscle", "tomato", "blueberry", "prejudice", "iphone"]
word = random.choice(words)

display = ["_"] * len(word)
lives = 13
guessed_letters = []

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Lives which are left:", lives)
    print("Letters you have said:", ", ".join(guessed_letters))

    guess = input("Guess a single letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("That's a correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("That's a wrong guess!")
        lives -= 1

if "_" not in display:
    print("\n You win! You were able to guess what the word is:", word)
else:
    print("\n You lose! The word was:", word)


