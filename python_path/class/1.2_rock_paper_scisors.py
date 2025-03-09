# attempt No. 1

'''rock = 'rock'
paper = 'paper'
scisors = 'scisors'
score_player_1 = 0
score_player_2 = 0
player_1 = input('Player 1 ')
player_2 = input('player 2 ')'''

'''if score_player_1 or score_player_2 < 3:
    if player_1 == rock and player_2 == paper:
        print('Point for player 2')
        score_player_2 + 1
        print(score_player_1)
        print(score_player_2)
    elif player_1 == rock and player_2 == scisors:
        print('Point for player 1')
        score_player_1 =+ 1
        print(score_player_1)
        print(score_player_2)
    elif player_1 == scisors and player_2 == paper:
        print('Point for player 1')
        score_player_1 + 1
        print(score_player_1)
        print(score_player_2)
    elif player_2 == rock and player_1 == paper:
        print('Point for player 1')
        score_player_1 + 1
        print(score_player_1)
        print(score_player_2)
    elif player_2 == rock and player_1 == scisors:
        print('Point for player 2')
        score_player_2 + 1
        print(score_player_1)
        print(score_player_2)
    elif player_2 == scisors and player_1 == paper:
        print('Point for player 2')
        score_player_2 + 1
        print(score_player_1)
        print(score_player_2)
    else:
        print('Try again')
        print(score_player_1)
        print(score_player_2)
else:
    if score_player_1 == 3:
        print('Player 1 Win')
    elif score_player_2 == 3:
        print('Player 2 Win')
    else:
        print('Keep playing')'''

# attempt No. 2

'''def rock_paper_scisors_game(player_1, player_2):
    if score_player_1 or score_player_2 < 3:
        if player_1 == rock and player_2 == paper:
            print('Point for player 2')
            score_player_2 + 1
            print(score_player_1)
            print(score_player_2)
        elif player_1 == rock and player_2 == scisors:
            print('Point for player 1')
            score_player_1 =+ 1
            print(score_player_1)
            print(score_player_2)
        elif player_1 == scisors and player_2 == paper:
            print('Point for player 1')
            score_player_1 + 1
            print(score_player_1)
            print(score_player_2)
        elif player_2 == rock and player_1 == paper:
            print('Point for player 1')
            score_player_1 + 1
            print(score_player_1)
            print(score_player_2)
        elif player_2 == rock and player_1 == scisors:
            print('Point for player 2')
            score_player_2 + 1
            print(score_player_1)
            print(score_player_2)
        elif player_2 == scisors and player_1 == paper:
            print('Point for player 2')
            score_player_2 + 1
            print(score_player_1)
            print(score_player_2)
        else:
            print('Try again')
            print(score_player_1)
            print(score_player_2)
    else:
        if score_player_1 == 3:
            print('Player 1 Win')
        elif score_player_2 == 3:
            print('Player 2 Win')
        else:
            print('Keep playing')
return'''

# attempt No. 3


def determine_winner(player_1, player_2):
    if player_1 == player_2:
        return 'Try again'
        #print('Try again')
    elif(player_1 == 'rock' and player_2 == 'scissors') or \
        (player_1 == 'scissors' and player_2 == 'paper') or \
        (player_1 == 'paper' and player_2 == 'rock'):
        return 'Point for player number 1'
        #print('Point for player number 1')
    else:
        return 'Point for player number 2'
        #print('Point for player number 2')

def play_game():
    player_1_score = 0
    player_2_score = 0

    while player_1_score < 3 and player_2_score < 3:
        #Get input for both players
        player_1 = input("Player 1: ").lower()
        player_2 = input("Player 2: ").lower()

        #Ensure both players make a valid choise
        if player_1 not in ['rock', 'paper', 'scissors'] or player_2 not in ['rock', 'paper', 'scissors']:
            print('Make a valid choise: rock, paper, or scissors')
            continue

        #Determine the winner of the round
        result = determine_winner(player_1, player_2)
        print(result)

        #Update scores based on the round resoult
        if result == 'Point for player number 1':
            player_1_score =+ 1
        elif result == 'Point for player number 2':
            player_2_score =+ 1

        #display de current scores
        print(f'Score player 1 = {player_1_score}, Score player 2 = {player_2_score}')

    if player_1_score == 3:
        print('Player 1 wins the game!')
    else:
        print('Player 2 wins the game!')

#Start the game
play_game()
