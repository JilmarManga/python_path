def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    player1_score = 0
    player2_score = 0

    while player1_score < 3 and player2_score < 3:
        # Get input from both players
        player1 = input("Player 1, choose rock, paper, or scissors: ").lower()
        player2 = input("Player 2, choose rock, paper, or scissors: ").lower()

        # Ensure both players make a valid choice
        if player1 not in ['rock', 'paper', 'scissors'] or player2 not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        # Determine the winner of the round
        result = determine_winner(player1, player2)
        print(result)

        # Update scores based on the round result
        if result == "Player 1 wins!":
            player1_score += 1
        elif result == "Player 2 wins!":
            player2_score += 1

        # Display current scores
        print(f"Score: Player 1 = {player1_score}, Player 2 = {player2_score}")

    # Declare the overall winner
    if player1_score == 3:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

# Start the game
play_game()