# Homework XVII
import random

def initialize_game():
    animals = ["owl", "cow", "sheep", "mouse", "chicken"]
    chosen_animal = random.choice(animals)
    return chosen_animal

def print_underscores(word):
    print("_" * len(word))

secret_word = initialize_game()
print_underscores(secret_word)



