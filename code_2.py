class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def check_win(self, player):
        win_conditions = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[3], self.board[4], self.board[5]],
            [self.board[6], self.board[7], self.board[8]],
            [self.board[0], self.board[3], self.board[6]],
            [self.board[1], self.board[4], self.board[7]],
            [self.board[2], self.board[5], self.board[8]],
            [self.board[0], self.board[4], self.board[8]],
            [self.board[2], self.board[4], self.board[6]],
        ]
        return [player, player, player] in win_conditions

    def check_tie(self):
        return ' ' not in self.board

    def get_player_move(self):
        move = -1
        while move not in range(1, 10) or self.board[move-1] != ' ':
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
        return move - 1

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        while True:
            self.print_board()
            move = self.get_player_move()
            self.board[move] = self.current_player

            if self.check_win(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            elif self.check_tie():
                self.print_board()
                print("It's a tie!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
