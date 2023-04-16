import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while guess_number != random_number:
        try:
            guess_number = int(input(f"Guess a number between 1 and {x}: "))
        except:
            print("Please enter a valid number")
        print(guess_number)
        if guess_number < random_number:
            print("Guess again. Too low")
        elif guess_number > random_number:
            print("Guess again. Too high!")       
    print(f"You guess the number right!. The correct number is {random_number}")

#guess(10)    


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if high != low:
            print(f"Guess a nuber between {low} and {high}")
            guess_number = random.randint(low,high)
        feedback = input(f"Is {guess_number} too high (h) or too low (l)")
        if feedback == "h":
            high = guess_number-1
        elif feedback == "l":
            low = guess_number+1
    print(f"you gessed the number correct {guess_number}")


computer_guess(25)