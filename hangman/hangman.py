import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word_to_guess = get_valid_word(words)
    letters_in_word = set(word_to_guess)
    guessed_letter = set()
    guessed_letter.add(random.choice(tuple(letters_in_word)))
    print(f"Word to guess: {word_to_guess}")

    
    while len(letters_in_word)>1:
        print(f"\nYou have guessed the following letters: ",", ".join(guessed_letter))
        guess = input("Guess a character: ").lower()
        if guess in guessed_letter:
            print(f"'{guess}' has already been guessed")
        if guess not in guessed_letter and guess in letters_in_word:
            letters_in_word.remove(guess)
        guessed_letter.add(guess)

        for l in word_to_guess:
            if l in guessed_letter:
                print(l,end='')
            else:
                print("_", end='')

hangman()