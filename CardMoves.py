from enum import Enum
from typing import Tuple

class PieceColor(Enum):
    RED = 1
    BLUE = 2

class Piece:
    color : PieceColor = None
    name : str = ''
    # location : Tuple = None
    is_king : bool = False
    is_empty : bool = False

    def __init__(self, is_empty=False, color=None, is_king=False, name=''):
        self.is_empty = is_empty
        self.color = color
        # self.location = location
        self.is_king = is_king
        self.name = name

    def __str__(self):
        if self.is_empty:
            return ' '
        elif self.color == PieceColor.RED:
            return 'R' if self.is_king else 'r'
        else:
            return 'B' if self.is_king else 'b'

    # def get_location(self):
    #     return self.location

    def get_color(self):
        return self.color

    def get_valid_moves(self, cards, board):
        return


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

    def get_moves(self, color, board_state):
        return self.moves


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

ALL_CARDS = [
    TIGER, DRAGON, FROG, RABBIT, 
    CRAB, ELEPHANT, GOOSE, ROOSTER,
    MONKEY, MANTIS, HORSE, OX, 
    CRANE, BOAR, EEL, COBRA
]
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

class Move:
    cards : list = []
    whose_move : PieceColor = None
    board : list = []

    def __init__(self, cards, whose_move, board):
        self.cards = cards
        self.whose_move = whose_move
        self.board = board

    # BLUE: UP = negative, RIGHT = positive
    # RED: UP = positive, RIGHT = negative
    def get_valid_moves(self):
        valid_moves = []
        for card in self.cards:
            moves = card.get_moves()
            for move in moves:
                break

        return None


class GameState:
    board : list = []
    whose_move : PieceColor = None
    blue_cards : list = []
    red_cards : list = []
    middle_card : GameCard = None
    move_history : list = []


    def update_state():
        return
