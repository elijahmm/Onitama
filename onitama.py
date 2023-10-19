from cardMoves import GameCard
import random
from enum import Enum
import numpy as np

class PieceColor(Enum):
    RED = 1
    BLUE = 2

class Piece:
    color : PieceColor = None
    name : str = ''
    loc : tuple = ()
    is_king : bool = False
    is_empty : bool = False

    def __init__(self, color, name, loc):
        self.color = color
        self.name = name
        self.loc = loc

    def __str__(self):
        if self.color == PieceColor.RED:
            return 'R' if self.is_king else 'r'
        else:
            return 'B' if self.is_king else 'b'

    def get_loc(self):
        return self.loc

    def get_color(self):
        return self.color

    def is_king(self):
        return 'king' in self.name

    # BLUE: UP = negative, RIGHT = positive
    # RED: UP = positive, RIGHT = negative
    def get_valid_moves(self, cards, board):
        for card in cards:
            break
        return


def build_cards():
    TIGER = GameCard('tiger', ['UU', 'D'])
    DRAGON = GameCard('dragon', ['URR', 'ULL', 'DR', 'DL'])
    FROG = GameCard('frog', ['UL', 'LL', 'DR'])
    RABBIT = GameCard('rabbit', ['DL', 'UR', 'RR'])

    CRAB = GameCard('crab', ['LL', 'RR', 'U'])
    ELEPHANT = GameCard('elephant', ['UR', 'UL', 'R', 'L'])
    GOOSE = GameCard('goose', ['UL', 'R', 'DR', 'L'])
    ROOSTER = GameCard('rooster', ['UR', 'R', 'DL', 'L'])

    MONKEY = GameCard('monkey', ['UL', 'UR', 'DL', 'DR'])
    MANTIS = GameCard('mantis', ['UL', 'UR', 'D'])
    HORSE = GameCard('horse', ['U', 'L', 'D'])
    OX = GameCard('ox', ['U', 'R', 'D'])

    CRANE = GameCard('crane', ['U', 'DL', 'DR'])
    BOAR = GameCard('boar', ['R', 'U', 'L'])
    EEL = GameCard('eel', ['UL', 'DL', 'R'])
    COBRA = GameCard('cobra', ['L', 'UR', 'DR'])

    return [
        TIGER, DRAGON, FROG, RABBIT, 
        CRAB, ELEPHANT, GOOSE, ROOSTER,
        MONKEY, MANTIS, HORSE, OX, 
        CRANE, BOAR, EEL, COBRA
    ]

def print_board(b):
    print('=====================')
    for row in range(5):

        print_str = ''
        for col in range(5):
            if b[row][col] is None:
                print_str += '  | '
            else:
                print_str += str(b[row][col]) + ' | '
        
        print(f'| {print_str}')
        if row != 4:
            print('---------------------')
        else: 
            print('=====================')


# set up board
def board_setup(): 
    piece_map = {}
    for x in range(0,5):
        if x == 2:
            name = 'red_king'
        else:
            name = f'red_pawn_{x}'
        piece_map[name] = Piece(color=PieceColor.RED, name=name, loc=(0,x))

    for x in range(0,5):
        if x == 2:
            name = 'blue_king'
        else:
            name = f'blue_pawn_{x}'
        piece_map[name] = Piece(color=PieceColor.BLUE, name=name, loc=(4,x))

    board = np.empty((5,5), dtype=Piece)
    # print(board)

    for piece in piece_map.values():
        x, y = piece.get_loc()
        board[x][y] = piece
    
    return board, piece_map



board, piece_map = board_setup()
print_board(board)
print(piece_map)

# choose 5 random cards
all_cards = build_cards()
randoms = []
while len(randoms) < 5:
    r = random.randint(0, len(all_cards)-1)
    if r not in randoms:
        randoms.append(r)

cards_in_play = []
for i in range(5):
    cards_in_play.append(all_cards[randoms[i]])

for i in range(5):
    print(str(cards_in_play[i]))



