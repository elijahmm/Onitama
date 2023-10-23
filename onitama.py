import random
from enum import Enum
import numpy as np

#=============== random helpers ===============#
def between(num, low, high):
    return low <= num and num <= high

def in_board(x, y):
    return between(x, 0, 4) and between(y, 0, 4)

#==============================================#
class GameCard:
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
    name: str = ''
    moves: list = []

    def __init__(self, name, moves):
        self.moves = moves
        self.name = name

    def __str__(self):
        return self.name

ALL_CARDS = {
    'tiger': GameCard('tiger', ['UU', 'D']),
    'dragon': GameCard('dragon', ['URR', 'ULL', 'DR', 'DL']),
    'frog': GameCard('frog', ['UL', 'LL', 'DR']),
    'rabbit': GameCard('rabbit', ['DL', 'UR', 'RR']),
    'crab': GameCard('crab', ['LL', 'RR', 'U']),
    'elephant': GameCard('elephant', ['UR', 'UL', 'R', 'L']),
    'goose': GameCard('goose', ['UL', 'R', 'DR', 'L']),
    'rooster': GameCard('rooster', ['UR', 'R', 'DL', 'L']),
    'monkey': GameCard('monkey', ['UL', 'UR', 'DL', 'DR']),
    'mantis': GameCard('mantis', ['UL', 'UR', 'D']),
    'horse': GameCard('horse', ['U', 'L', 'D']),
    'ox': GameCard('ox', ['U', 'R', 'D']),
    'crane': GameCard('crane', ['U', 'DL', 'DR']),
    'boar': GameCard('boar', ['R', 'U', 'L']),
    'eel': GameCard('eel', ['UL', 'DL', 'R']),
    'cobra': GameCard('cobra', ['L', 'UR', 'DR']),
}

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
                if in_board(new_x, new_y) and (board[new_y][new_x] is None or board[new_y][new_x].color != self.color):
                        valid_moves.append((new_x, new_y, card.name, move))

        return valid_moves

class GameState:
    board : list = []
    whose_move = None
    cards : dict = {}
    middle_card : GameCard = None
    move_history : list = []

    def __init__(self, board, whose_move, cards_in_play):
        self.board = board
        self.whose_move = whose_move
        self.cards = {
            PieceColor.BLUE: cards_in_play[:2],
            PieceColor.RED: cards_in_play[3:],
            'mid': cards_in_play[2]
        }
        self.move_history = []

    def print_board(self):
        b = self.board
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

    def get_moves(self):
        valid_moves = {}
        for row in self.board:
            for piece in row:
                if piece is not None and piece.color == self.whose_move:
                    valid_moves[piece.loc] = piece.get_valid_moves(self.cards[piece.color], self.board)
        return valid_moves

    def update_whose_move(self):
        if self.whose_move == PieceColor.RED:
            self.whose_move = PieceColor.BLUE
        else: 
            self.whose_move = PieceColor.RED
    
    def update_state(self, card_used: str):
        cards_possible_to_use = self.cards[self.whose_move]
        for idx, card in enumerate(cards_possible_to_use):
            if card.name == card_used:
                self.cards[self.whose_move][idx] = self.cards['mid']
                self.cards['mid'] = card
                break

        self.update_whose_move()       

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
#print(piece_map)

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
    
TIGER = GameCard('tiger', ['UU', 'D'])
DRAGON = GameCard('dragon', ['URR', 'ULL', 'DR', 'DL'])
FROG = GameCard('frog', ['UL', 'LL', 'DR'])
RABBIT = GameCard('rabbit', ['DL', 'UR', 'RR'])
CRAB = GameCard('crab', ['LL', 'RR', 'U'])

cards_in_play = all_cards
game_state = GameState(board, PieceColor.RED, [TIGER, DRAGON, FROG, RABBIT, CRAB])
print()
print('*O==N==I==T==A==M==A*')
game_state.print_board()
print()
for card in [TIGER, DRAGON, FROG, RABBIT, CRAB]:
    print(f'{card} --> {card.moves}')

print(f'{"RED" if game_state.whose_move == PieceColor.RED else "BLUE"}\'S VALID MOVES')
moves = game_state.get_moves()
for k, v in moves.items():
    print(f'{k} --> {v}')

# game_in_play = True
# whose_turn = PieceColor.RED
# while game_in_play:
    
#     player_move = int(
#         input(
#             f'It is {"Blue" if whose_turn == PieceColor.BLUE else "Red"}\'s turn\n Which move do you select? '
#         )
#     )
#     if between(player_move, 0, len(valid_moves_red)-1):
#         print('Great')

#     else: 
#         raise ValueError('Invalid Move')














# Expansion pack cards
# OTTER = GameCard('otter', [])
# PHOENIX = GameCard('phoenix', []) 
# TURTLE = GameCard('turtle', [])
# IGUANA = GameCard('iguana', [])
# SABLE = GameCard('sable', [])
# PANDA = GameCard('panda', [])
# BEAR = GameCard('bear', [])
# FOX = GameCard('fox', [])
# GIRAFFE = GameCard('giraffe', [])
# KIRIN = GameCard('kirin', [])
# RAT = GameCard('rat', [])
# TANUKI = GameCard('tanuki', [])
# MOUSE = GameCard('mouse', [])
# VIPER = GameCard('viper', [])
# SEASNAKE = GameCard('seasnake', [])
# DOG = GameCard('dog', [])