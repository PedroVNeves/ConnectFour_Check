class ConnectFour:
    def __init__(self, board: list[list[str]]):
        self.board = board
        self.num_x = 0
        self.num_o = 0
        self.rows = len(board)
        self.cols = len(board[0])
        self.x_wins = 0
        self.o_wins = 0
        
    def verify(self):
        if self.verify_symbols() and self.verify_empty_space() and self.verify_num_of_symbols():
            return self.verify_winner()
        else:
            return 'INVALID'   
    
    def verify_symbols(self):
        for line in self.board:
            for symbol in line:
                if symbol.lower() not in 'xo.':
                    return False
        return True
    
    def verify_empty_space(self):
        for i in range(self.rows - 1):
            for j in range(self.cols):
                if self.board[i][j].lower() != '.' and self.board[i+1][j].lower() == '.':
                    return False
        return True

    def verify_num_of_symbols(self):
        for line in self.board:
            for symbol in line:
                if symbol.lower() == 'x':
                    self.num_x += 1 
                elif symbol.lower() == 'o':
                    self.num_o += 1
        return abs(self.num_x - self.num_o) <= 1

    def verify_winner(self) -> str:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0,  -1),          (0, 1),
                      (1,  -1), (1, 0),  (1, 1)]

        for i in range(self.rows):
            for j in range(self.cols):
                symbol = self.board[i][j].lower()
                if symbol == '.':
                    continue
                for dx, dy in directions:
                    count = 1
                    x, y = i, j
                    for _ in range(3):
                        x += dx
                        y += dy
                        if 0 <= x < self.rows and 0 <= y < self.cols and self.board[x][y].lower() == symbol:
                            count += 1
                        else:
                            break
                    if count == 4:
                        if symbol == 'x':
                            self.x_wins += 1
                        elif symbol == 'o':
                            self.o_wins += 1
        
        if self.x_wins > 0 and self.o_wins > 0:
            return 'INVALID'
        elif self.x_wins > 0:
            return 'VALID X'
        elif self.o_wins > 0:
            return 'VALID O'
        else:
            return 'VALID'


final_board = []
for i in range(6):
    line = list(input(f'Put the line {i+1}'))
    final_board.append(line)
    
board = ConnectFour(final_board)
print(board.verify())



