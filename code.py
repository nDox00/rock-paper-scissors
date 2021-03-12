def play_now():
    print("Welcome to Rock, Paper Scissors")
    
    play = input("Do you wanna play? Y/N").title()    
    if play == 'Y':
        start = True
    elif play == 'N':
        start = False
    return start
  
from random import randint
def rock_paper_scissors():
    while True:
        print("1: Rock,\n 2: Paper, \n 3: Scissors")
        player_choice = int(input("Chose: "))
        if player_choice <= 3:
            print("That's Okay")
        else:
            if player_choice >=4:
                print("Invalid Choice, try again")
                continue
        
            
        

        pc_choice = randint(1,3)
    
        if player_choice == pc_choice:
            print("It's a tie!")
    
        elif player_choice == 3 and pc_choice == 2 or player_choice ==1:
            print("Player Wins!! Woop woop")
        else:
            print('Robocop wins :(')

            print(f'Your choice is {player_choice}')
            print(f'PC choice is {pc_choice}')
