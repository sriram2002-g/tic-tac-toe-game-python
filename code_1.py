# Tic-Tac-Toe Game in Python

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a win
def check_win(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

# Check for a tie
def check_tie(board):
    return ' ' not in board

# Get player move
def get_player_move(board, player):
    move = -1
    while move not in range(1, 10) or board[move-1] != ' ':
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    return move - 1

# Switch player
def switch_player(player):
    return 'O' if player == 'X' else 'X'

# Main game function
def play_game():
    board = initialize_board()
    current_player = 'X'
    
    while True:
        print_board(board)
        move = get_player_move(board, current_player)
        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    play_game()
