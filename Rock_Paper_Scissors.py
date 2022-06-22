import random

# The variables below store the ascii art of rock, paper, scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

# Start of the code for the game.
play_again = 'Y'
count_win = 0 # count_win counts how many times the users have won.
games_played = 0 # games_played counts the total number of games the user has played.
while play_again.upper() == 'Y':
    user_choice = 3
    games_played += 1
    while user_choice < 0 or user_choice > 2:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    comp_choice = random.randint(0, 2)
    print("You chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[comp_choice])
    if user_choice == comp_choice:
        print("It's a draw.")
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
        count_win += 1
    elif user_choice > comp_choice:
        print("You win!")
        count_win += 1
    else:
        print("Computer wins!")
    play_again = 'A'
    while play_again.upper() != 'Y' and play_again.upper() != 'N':
        play_again = input("Do you want to play again? Y or N\n")
        if (play_again.upper() != 'Y' and play_again.upper() != 'N'):
            print("Invalid input. Please input Y/N")
win_rate = (float(count_win) / float(games_played)) * 100
print("You won {:.0f} out of {:.0f} games. Your win rate is {:.2f}%".format(count_win, games_played, win_rate))
print("Thank you for playing!")