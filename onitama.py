from cardMoves import Piece, PieceColor, GameCard
import random


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

    ALL_CARDS = [
        TIGER, DRAGON, FROG, RABBIT, 
        CRAB, ELEPHANT, GOOSE, ROOSTER,
        MONKEY, MANTIS, HORSE, OX, 
        CRANE, BOAR, EEL, COBRA
    ]
    return ALL_CARDS

def print_board(b):
    print('=====================')
    for row in range(5):

        print_str = ''
        for col in range(5):
            print_str += str(b[row][col]) + ' | '
        
        print(f'| {print_str}')
        if row != 4:
            print('---------------------')
        else: 
            print('=====================')


# set up board
def board_setup(): 
    board = []
    red_start = [
        Piece(color=PieceColor.RED, is_king=False),
        Piece(color=PieceColor.RED, is_king=False),
        Piece(color=PieceColor.RED, is_king=True),
        Piece(color=PieceColor.RED, is_king=False),
        Piece(color=PieceColor.RED, is_king=False)
    ]
    blue_start = [
        Piece(color=PieceColor.BLUE, is_king=False),
        Piece(color=PieceColor.BLUE, is_king=False),
        Piece(color=PieceColor.BLUE, is_king=True),
        Piece(color=PieceColor.BLUE, is_king=False),
        Piece(color=PieceColor.BLUE, is_king=False)
    ]
    board.append(red_start)
    for _ in range(3):
        row = []
        for _ in range(5):
            row.append(Piece(is_empty=True))
        board.append(row)
    board.append(blue_start)

    return board

board = board_setup()
print_board(board)

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



