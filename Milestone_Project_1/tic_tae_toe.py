def players_roles():
    while True:
        player1 = input(" Player1 choose 'O' or 'X'").upper()
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            print("Invalid Input .!!!")

    
    return player1,player2

def player_ready():
    while True:
        ready = input("Are you ready to play the game YES or NOT.??").upper()
        if ready in ['YES','NO']:
            break
        else:
            print("Invalid Input..!!")

    return ready
def choose_pos(board):
    while True:
        try:
            position = int(input("Enter the position from (1-9): "))
            if position in range(1, 10):
                if board[position - 1] == ' ':
                    return position
                else:
                    print("That position is already taken. Choose another one.")
            else:
                print("Invalid input. Please enter a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def win_combos(board,current_player):
    combos = [(0,1,2),(3,4,5),(6,7,8),
              (0,3,6),(1,4,7),(2,5,8),
              (0,4,8),(2,4,6)]
    
    for a,b,c in combos:
        if board[a]==current_player and board[b]==current_player and board[c] ==  current_player:
            return(f"{current_player} you have won the game .!!!!!")


def isfull(board):
    return ' ' not in board



ready = player_ready()
board = [' '] * 9
Player1,Player2 = players_roles()
current_player=" "
current_player= Player1
if ready == 'YES':
    while(True):
        
        pos = choose_pos(board)
        board[pos-1]= current_player
        display_board(board)
        win = win_combos(board,current_player)
        if(win != None):
            display_board(board)
            print(win)
            break
        elif isfull(board):
            display_board(board)
            print("The game is draw")
        else:
            if current_player == Player1:
                current_player = Player2
            else:
                current_player= Player1

            



else:
    print("Come Soon..!!!")            






