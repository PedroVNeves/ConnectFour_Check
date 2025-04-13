class ConnectFour:
    """Class to validate and analyze a Connect Four game board."""

    def __init__(self, board: list[list[str]]):
        """
        Initializes the game board and internal counters.

        Args:
            board (list[list[str]]): 2D list representing the game board.
        """
        self.board = board
        self.num_x = 0  # Counts how many 'x' pieces there are
        self.num_o = 0  # Counts how many 'o' pieces there are
        self.rows = len(board)
        self.cols = len(board[0])
        self.x_wins = 0  # Number of winning lines for 'x'
        self.o_wins = 0  # Number of winning lines for 'o'

    def verify(self) -> str:
        """
        Runs all checks to determine if the board is valid and who won.

        Returns:
            str: 'INVALID', 'VALID', 'VALID X', or 'VALID O'
        """
        # All checks must pass: valid symbols, proper stacking, and move count
        if self.verify_symbols() and self.verify_empty_space() and self.verify_num_of_symbols():
            return self.verify_winner()
        else:
            return 'INVALID'

    def verify_symbols(self) -> bool:
        """
        Checks if all board characters are valid ('x', 'o', or '.').

        Returns:
            bool: True if valid, False if any invalid symbol is found.
        """
        for line in self.board:
            for symbol in line:
                if symbol.lower() not in 'xo.':
                    return False  # Found an invalid symbol
        return True

    def verify_empty_space(self) -> bool:
        """
        Makes sure no piece is "floating" above an empty cell.

        Returns:
            bool: True if all pieces are properly stacked, False otherwise.
        """
        for i in range(self.rows - 1):
            for j in range(self.cols):
                # A piece can't be placed above an empty spot
                if self.board[i][j].lower() != '.' and self.board[i + 1][j].lower() == '.':
                    return False
        return True

    def verify_num_of_symbols(self) -> bool:
        """
        Counts 'x' and 'o' to check if the turn order makes sense.

        Returns:
            bool: True if the count difference is 0 or 1, False otherwise.
        """
        for line in self.board:
            for symbol in line:
                if symbol.lower() == 'x':
                    self.num_x += 1
                elif symbol.lower() == 'o':
                    self.num_o += 1
        # Players must take turns, so difference must be at most 1
        return abs(self.num_x - self.num_o) <= 1

    def verify_winner(self) -> str:
        """
        Checks for any winning lines and determines the result.

        Returns:
            str: 'VALID', 'VALID X', 'VALID O', or 'INVALID' if both players won.
        """
        # All 8 directions to check for a line of 4
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1), (1, 0),  (1, 1)]

        for i in range(self.rows):
            for j in range(self.cols):
                symbol = self.board[i][j].lower()
                if symbol == '.':
                    continue  # Skip empty cells
                for dx, dy in directions:
                    count = 1
                    x, y = i, j
                    for _ in range(3):
                        x += dx
                        y += dy
                        # Check if we're still on the board and if the line continues
                        if 0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y].lower() == symbol:
                            count += 1
                        else:
                            break
                    if count == 4:
                        # Mark the win for the player
                        if symbol == 'x':
                            self.x_wins += 1
                        elif symbol == 'o':
                            self.o_wins += 1

        # Only one player can win in a valid game
        if self.x_wins > 0 and self.o_wins > 0:
            return 'INVALID'
        elif self.x_wins > 0:
            return 'VALID X'
        elif self.o_wins > 0:
            return 'VALID O'
        else:
            return 'VALID'


# Reading the board from user input
final_board = []
for i in range(6):
    line = list(input(f'Enter line {i + 1}: '))
    final_board.append(line)

# Create the game instance and check result
board = ConnectFour(final_board)
print(board.verify())