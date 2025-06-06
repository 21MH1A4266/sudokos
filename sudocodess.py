def is_valid_group(group):
    """Check if a group (row, column, or zone) contains unique digits from 1 to 9."""
    return sorted(group) == list(range(1, 10))

def is_valid_sudoku(board, custom_zones=None):
    """Validate a 9x9 Sudoku board with optional custom zones."""
    # Check rows and columns
    for i in range(9):
        if not is_valid_group(board[i]):
            return False
        if not is_valid_group([board[j][i] for j in range(9)]):
            return False

    # Check 3x3 subgrids
    for i in range(3):
        for j in range(3):
            subgrid = [board[i*3 + m][j*3 + n] for m in range(3) for n in range(3)]
            if not is_valid_group(subgrid):
                return False

    # Check custom zones if provided
    if custom_zones:
        for zone in custom_zones:
            zone_values = [board[i][j] for i, j in zone]
            if not is_valid_group(zone_values):
                return False

    return True
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

custom_zones = [
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
    [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
    [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
]
print(is_valid_sudoku(board, custom_zones)) 
