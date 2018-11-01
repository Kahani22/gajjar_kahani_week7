from random import randint

player_lives = 5
computer_lives = 5

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# define a win or lose function instead of the procedural way


def winorlose(status):
    # handle win or lose based on the status we pass in
    print("Called the win or lose function")
    print("===============================")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N: ")

    if choice == "Y" or choice == "y":

        # reset the game
        # change global variables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5

    elif choice == "n" or choice == "N":
        exit()


while player is False:
    print("=============")
    print("player Lives:", player_lives, "/5")
    print("AI Lives:", computer_lives, "/5")
    print("=============")

    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses", player)

    # check to see if you chose the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            # computer won
            player_lives -= 1
            print("You lose!", computer, "covers", player, "\n")
        else:
            print("You win!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            player_lives -= 1
            print("You lose!", computer, "cuts", player, "\n")
            computer_lives -= 1
        else:
            print("You won!", player, "covers", computer, "\n")

    elif player == "Scissors":
        if computer == "Rock":
            player_lives -= 1
            print("You lose!", computer, "smashes", player, "\n")
            computer_lives -= 1
        else:
            print("You win!", player, "cuts", computer, "\n")

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

        # checking win/lose and functions
    if player_lives == 0:
            winorlose("lost")
    elif computer_lives == 0:
            winorlose("won")

    player = False
    computer = choices[randint(0, 2)]
