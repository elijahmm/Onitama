from curses import COLOR_BLACK


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
    name: str = ''
    moves: list = []

    def __init__(self, name, moves):
        self.all_moves = moves
        self.name = name

    def get_valid_moves(self, board_state):
        return self.all_moves

OX = GameCard('ox', ['U', 'R', 'D'])
HORSE = GameCard('horse', ['U', 'L', 'D'])
DRAGON = GameCard('dragon', ['URR', 'ULL', 'DR', 'DL'])
COBRA = GameCard('cobra', ['L', 'UR', 'DR'])
ROOSTER = GameCard('rooster', ['UR', 'R', 'DL', 'L'])
FROG = GameCard('frog', ['UL', 'LL', 'DR'])
ELEPHANT = GameCard('elephant', ['UR', 'UL', 'R', 'L'])
MANTIS = GameCard('mantis', ['UL', 'UR', 'D'])
GOOSE = GameCard('goose', ['UL', 'R', 'DR', 'L'])
OTTER = GameCard('otter', [])
PHOENIX = GameCard('phoenix', []) 
TURTLE = GameCard('turtle', [])
IGUANA = GameCard('iguana', [])
SABLE = GameCard('sable', [])
PANDA = GameCard('panda', [])