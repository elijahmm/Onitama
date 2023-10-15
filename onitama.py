from curses import ALL_MOUSE_EVENTS


cards = []

b = [
    ['r', 'r', 'R', 'r', 'r'],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    ['b', 'b', 'B', 'b', 'b']
]

# odd signifies red pieces
# even signifies blue pieces

def print_board(b):
    print('========================')
    for row in range(5):
        print_str = ''
        for 
        print_str = '|' + b[row][col] for col in range(5)
        print(f'|{b[row][0]}|{b[row][1]}|{b[2][row]}|{b[3][row]}|{b[4][row]}|')
        if row != 4:
            print('------------------------')
        else: 
            print('========================')


print_board(b)


class GameCard():
    '''
    2 = current position
    1 = valid jumps/moves
    Example: Ox (3 valid moves 1up, 1right, 1down)
    [0, 0, 0, 0, 0]
    [0, 0, 1, 0, 0]
    [0, 0, 2, 1, 0] 
    [0, 0, 1, 0, 0] 
    [0, 0, 0, 0, 0]
    '''

    def get_valid_moves(self, board_state):
        return self.all_moves
 