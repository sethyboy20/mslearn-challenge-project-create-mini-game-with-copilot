# Create a multiplayer Rock Paper Scissors game where the user can play against the computer
# The player can choose one of the three options 'rock", "paper", or "scissors" and should be warned if they enter an invalid option.
# The computer should randomly select one of the three options and the winner should be determined based on the rules of the game.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# The game should keep track of the score of the player and the computer and display it at the end of each round.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# The game should end when the player decides to stop playing.
# The player should be able to play as many rounds as they want.

import random

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    while True:
        player_choice = input('Enter your choice (rock, paper, scissors): ')
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        if player_choice.lower() not in ['rock', 'paper', 'scissors']:
            print('Invalid option. Please enter rock, paper, or scissors.')
            continue
        print(f'Player: {player_choice}')
        print(f'Computer: {computer_choice}')
        if player_choice == computer_choice:
            print('It\'s a tie!')
        elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
            print('Player wins!')
            player_score += 1
        else:
            print('Computer wins!')
            computer_score += 1
        print(f'Player: {player_score} - Computer: {computer_score}')
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            break

rock_paper_scissors()