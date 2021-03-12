from random import randint
def rock_paper_scissors():
    print("Welcome to Rock, Paper Scissors")
    
    play = input("Do you wanna play? Y/N").title()    
    if play == 'Y':
        start = True
    elif play == 'N':
        start = False
        print("Thank you for playing")

    while start == True:
        print(" 1: Rock,\n 2: Paper, \n 3: Scissors")
        player_choice = int(input("Chose: "))
        if player_choice <= 3:
            print("That's Okay")
        else:
            if player_choice >=4:
                print("Invalid Choice, try again")
                continue
        pc_choice = randint(1,3)
        print(f'Your choice is {player_choice}')
        print(f'PC choice is {pc_choice}')
   
    
        if player_choice == pc_choice:
            print("It's a tie!")
    
        elif player_choice == 3 and pc_choice == 2 or player_choice ==2 and pc_choice == 1 or player_choice ==1 and pc_choice == 3 :
            print("Player Wins!! Woop woop")
        else:
            print('Robocop wins :(')
        
        break
        
    play_again = input("Do you want to play again? Y/N")
    play_again = play
    
