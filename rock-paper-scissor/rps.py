import random

def play():
    userSelection = input("Please select Rock (R), Paper (P) or Scissor (S): ").upper()
    while len(userSelection)>1 or userSelection not in {'R','P','S'}:
        print("Please enter valid selection")
        userSelection = input("Please select Rock (R), Paper (P) or Scissor (S): ").upper()

    computerSelection = random.choice(['R', 'P', 'S'])
    print(f"Computer selection: {computerSelection}")

    if userSelection == computerSelection:
        return "It is a tie"
    
    if getWinner(userSelection,computerSelection):
        return "Yow won"
    
    return "You Lost"


def getWinner(player, opponent):
    
    #Rules R>S P>R S>P    
    if (player == "R" and opponent=="S") or (player == "P" and opponent=="R") or (player == "S" and opponent=="P"):
        return True
    

print(play())