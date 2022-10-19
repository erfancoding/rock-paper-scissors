# Rock Paper Scissors Game
import random
game_images = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]


game_options = ['rock', 'paper', 'scissors']
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice = random.randint(0, len(game_options)-1)

if user_choice > 2 or user_choice < 0:
    print("You have entered an invalid number. You lose!")
else:

    print("You chose:", game_images[user_choice], sep="\n")
    print("Computer chose:", game_images[computer_choice], sep="\n")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
