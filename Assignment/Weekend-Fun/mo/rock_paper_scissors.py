player1 = input("Player 1: Enter rock, paper or scissors: ")
player2 = input("Player 2: Enter rock, Paper or scissors: ")

if(player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock" or player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins")
elif(player1 == "rock" and player2 == "paper" or player1 == "paper" and player2 == "scissors" or player1 == "scissors" and player2 == "rock"):
    print("Player 2 wins")
else:
    print("Tie")
