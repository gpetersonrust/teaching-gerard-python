import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("rock, paper, or scissors? (or type 'exit' to quit) ").lower()

    if player == "exit":
        break

    if player in choices:
        computer = random.choice(choices)
        print("You chose", player, "and the computer chose", computer)

        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lose!")
            else:
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
                print("You lose!")
            else:
                print("You win!")
        elif player == "scissors":
            if computer == "rock":
                print("You lose!")
            else:
                print("You win!")

        if input("Do you want to play again? Yes or No ").lower() == "no":
            break
    else:
        print("Invalid choice, please try again.")
