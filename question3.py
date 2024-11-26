import random

def scramble(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    result = "".join(word_letters)
    return result
def get_user_input():
    while True:
        user_input = input("Enter your guess: ")
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid input! Please enter a text value")


words_list = ["apple", "car", "flower", "window"]
rand_word = random.choice(words_list)
print("Welcome to the Word Scramble Game!")
print("Try to guess the original word from the scrambled word: " + scramble(rand_word))
print("You have 5 attempts.")

attemps = 5

while attemps:
    user_guess = get_user_input()
    
    if user_guess == rand_word:
        print("Congratulations! You guessed the correct word!")
        break
    else:
        attemps -= 1
        print(f"Incorrect! Try again. You have {attemps} attempts left")

if attemps == 0:
    print(f"You’re out of attempts! The correct word was: {rand_word}")

        
