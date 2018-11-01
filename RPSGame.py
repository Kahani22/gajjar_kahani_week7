from random import randint

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5


# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("computer chooses", computer)

# set up our loop
while player is False:
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses", player)

    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            # computer won
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You won!", player, "covers", computer)

    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

        #checking win/lose
        if player_lives is 0:
            print("Zero lives, play again?")

            choice = input("Y / N? ")

            if choice == "Y" or choice == "y":
                player_lives = 5
                computer_lives = 5
                player = False
                computer = choices[randint(0,2)]
            elif choice == "N" or choice =="n":
                print("you've had enough losing")
                exit()

                if computer_lives is 0:
            print("computer out of lives, play again?")

            choice = input("Y / N? ")

            if choice == "Y" or choice == "y":
                player_lives = 5
                computer_lives = 5
                player = False
                computer = choices[randint(0,2)]
            elif choice == "N" or choice =="n":
                print("you've had enough losing")
                exit()

    player = False
    computer = choices[randint(0, 2)]

