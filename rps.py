from random import choice

print('...Rock... \n...Paper... \n...Scissors...')
p1_score = 0
p2_score = 0
winning_score = 3

while p1_score < winning_score and p2_score < winning_score:
    print(f'Player 1 Score: {p1_score}\nPlayer 2 Score: {p2_score}')
    computer = choice(['rock', 'paper', 'scissors'])
    player1 = input('What is your choice? ').lower()
    player2 = computer
    if player1 == 'quit' or player1 == 'q':
        break
    if player1 == 'rock' or player1 == 'paper' or player1 == 'scissors':
        print(f'Player 1 Chose: {player1} \nPlayer 2 Chose: {player2}')
        if (player1 == 'rock' and player2 == 'paper') or (player1 == 'scissors' and player2 == 'rock') or (player1 == 'paper' and player2 == 'scissors'):
            print('Player 2 Wins!!! \n')
            p2_score += 1
        elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
            print('Player 1 Wins!!! \n')
            p1_score += 1
        else:
            print('It\'s a Draw!!!\n')
    else:
        print('Please choose between rock, paper, or scissors\n')

if p1_score > p2_score:
    print('Congrats You Win!!')
elif p1_score == p2_score:
    print('You tied!')
else:
    print('Oh no You lost!')

print(f'Final Score\nPlayer 1 Score: {p1_score}\nPlayer 2 Score: {p2_score}')


############################################

# if player1 == 'rock' or player1 == 'paper' or player1 == 'scissors':
#   if player1 == 'rock':
#     if player2 == 'scissors':
#       print('Player 1 Wins!!!')
#     elif player2 == 'paper':
#       print('player 2 Wins')
#   elif player1 == 'paper':
#     if player2 == 'scissors':
#       print('Player 2 Wins!!!')
#     elif player2 == 'rock':
#       print('Player 1 Wins!!!')
#   elif player1 == 'scissors':
#     if player2 == 'rock':
#       print('Player 2 Wins!!!')
#     elif player2 == 'paper':
#       print('Player 1 Wins!!!')
#   else:
#     print('It\'s a Draw!!!')
# else:
#   print('Please choose between rock, paper, or scissors')

#######################################

# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")

# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")
