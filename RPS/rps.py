import random

def get_choices():
    player_choices = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices,  "computer": computer_choices}
    return choices
def check_win(player, computer):
    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
        return "Its a Tie!"
    elif player == "rock":
        if computer == "scissors":
            return "rock crushes scissor! you win!"
        else:
            return "paper covers rock! you lose!"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cut paper! you lose!"
    elif player == "scissors":
        if computer == "paper":
            return "scissor cuts paper! you win!"
        else:
            return "rock crushes scissor! you lose!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print (result)


