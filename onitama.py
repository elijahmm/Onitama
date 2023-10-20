from cardMoves import GameCard, GameState
import random
from enum import Enum
import numpy as np

def in_board(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5

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

    def is_king(self):
        return 'king' in self.name

    # BLUE: UP = negative, RIGHT = positive
    # RED: UP = positive, RIGHT = negative
    def get_valid_moves(self, cards, board):
        valid_moves = []
        for card in cards:
            for move in card.moves:
                x, y = self.loc
                x_dir, y_dir = 0, 0
                for c in move:
                    if c == 'U':
                        y_dir += 1
                    elif c == 'D': 
                        y_dir -= 1
                    elif c == 'L':
                        x_dir += 1
                    elif c == 'R':
                        x_dir -= 1
                        
                new_x = x + x_dir if self.color == PieceColor.RED else x - x_dir
                new_y = y + y_dir if self.color == PieceColor.RED else y - y_dir
                # print(f'{new_x=}, {new_y=}')
                if in_board(new_x, new_y):
                    if board[new_y][new_x] is None or board[new_y][new_x].color != self.color:
                        valid_moves.append((new_x, new_y, card.name, move))

        return valid_moves


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


# set up board
def board_setup(): 
    piece_map = {}
    for x in range(0,5):
        if x == 2:
            name = 'red_king'
        else:
            name = f'red_pawn_{x}'
        piece_map[name] = Piece(color=PieceColor.RED, name=name, loc=(x,0))

    for x in range(0,5):
        if x == 2:
            name = 'blue_king'
        else:
            name = f'blue_pawn_{x}'
        piece_map[name] = Piece(color=PieceColor.BLUE, name=name, loc=(x,4))

    board = np.empty((5,5), dtype=Piece)
    # print(board)

    for piece in piece_map.values():
        x, y = piece.loc
        board[y][x] = piece
    
    return board, piece_map


board, piece_map = board_setup()
print(piece_map)

# choose 5 random cards
all_cards = build_cards()
def get_5_random_cards():
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
    return cards_in_play

cards_in_play = all_cards
game_state = GameState(board, PieceColor.RED, cards_in_play[0:2], cards_in_play[3:5], cards_in_play[2], [])
game_state.print_board()
board = game_state.board
valid_moves = {} # piece at loc --> valid moves
for row in board:
    for piece in row:
        if piece is not None:
            cards = game_state.red_cards if piece.color == PieceColor.RED else game_state.blue_cards
            valid_moves[piece.loc] = piece.get_valid_moves(cards, board)
print('CARD MOVES')      
for card in cards_in_play[0:6]:
    print(f'{card} --> {card.moves}')

print('VALID MOVES')
for k, v in valid_moves.items():
    print(f'{k} --> {v}')
