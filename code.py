def play():
    print("Welcome to Rock, Paper Scissors")
    
    play = input("Do you wanna play? Y/N").title()    
    if play == 'Y':
        start = True
    elif play == 'N':
        print("That's Okay!, next time")
        start = False
        
    return start


def play_again():
    answer = input("Do you want to play again? Y/N").title()
    if answer == 'Y':
        answer = True
        print("Playing..")
    else:
        answer = False
        print("Thank you for playing")
    return answer

def rock_paper_scissors():   
        from random import randint
        pc_choice = randint(1,3)
        print(f'Your choice is {player}')
        print(f'PC choice is {pc_choice}')
   
    
        if player == pc_choice:
            print("It's a tie!")
            
        elif player == 3 and pc_choice == 2 or player ==2 and pc_choice == 1 or player ==1 and pc_choice == 3 :
            print("Player Wins!! Woop woop")
           
        else:
            print('Robocop wins :(')

            
 def player_choice():
    print(" 1: Rock,\n 2: Paper, \n 3: Scissors")
    player_choice = int(input("Chose: "))
    if player_choice <= 3:
        print("That's Okay")
    elif player_choice >=4:
        print("Invalid Choice, try again")
    return player_choice
                      
   
##Game 

play()
while True:
    player = player_choice()
    rock_paper_scissors()
    
    test = play_again()
    if test == False:
        break
