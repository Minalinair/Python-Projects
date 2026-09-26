import random
print("!!Welcome to Rock Paper Scissors game!!")
while True:
    player = input("Enter your choice (rock,paper or scissors):").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"You chose {player}")
    print(f"Computer chose {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer =="paper":
            print("You win!!")
        else:
            print("You lose!")
    elif player =="paper":
        if computer =="rock":
            print("You win!!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer =="paper":
            print("You win!!")
        else:
            print("You lose!")
    else:
        print("Invalid choice!Please choose rock, paper, or scissors.")
