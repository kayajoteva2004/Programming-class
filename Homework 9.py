import random

words = ["skincare", "chess", "literature", "dog", "mathematics", "Interstellar"]
word = random.choice(words)

display = ["_"] * len(word)
lives = 10
guessed_letters = []

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Lives left:", lives)

    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong!")
        lives -= 1

if "_" not in display:
    print("\n You win! The word is:", word)
else:
    print("\n You lose! The word was:", word)
