import random
GRID_SIZE = 8
board = [['.' for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# Directions for ray movements
DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Fire a ray from the given edge and trace its path
def fire_ray(board, entry_point, direction):
    x, y = entry_point

    # Move ray based on its direction
    dx, dy = direction

    while 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        if board[x][y] == 'A':  # Atom hit
            return "Absorbed"

        # Logic to handle deflection and reflection (you'll implement this)
        # ...

        # Move the ray
        x += dx
        y += dy

    # Ray exits from a different edge (or reflects back)
    return (x, y)

def is_adjacent_to_atom(board, x, y):
    # Check all adjacent cells
    adjacent_coords = [
        (x-1, y), (x+1, y), (x, y-1), (x, y+1)
    ]
    for ax, ay in adjacent_coords:
        if 0 <= ax < GRID_SIZE and 0 <= ay < GRID_SIZE:
            if board[ax][ay] == 'A':
                return True
    return False
# Defining the game board.

def guess_atom_position(board, x, y):
    if board[x][y] == 'A':
        return True
    return False
def display_board(board, reveal=False):
    for row in board:
        print(" ".join(row if reveal else ['.' if cell == 'A' else cell for cell in row]))

# Place 'n' atoms randomly inside the grid
def place_atoms(board, num_atoms):
    count = 0
    while count < num_atoms:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if board[x][y] == '.':
            board[x][y] = 'A'
            count += 1
class BlackBoxGame:
    def __init__(self, grid_size, num_atoms):
        self.grid_size = grid_size
        self.board = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.num_atoms = num_atoms
        place_atoms(self.board, self.num_atoms)

    def fire_ray(self, entry_point, direction):
        return fire_ray(self.board, entry_point, direction)

    def guess_atom(self, x, y):
        return guess_atom_position(self.board, x, y)

    def display(self, reveal=False):
        display_board(self.board, reveal)

