assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins,
    # group the twins and get rid of permutations
    naked_twin_list = [box for box in boxes if len(values[box]) == 2]
    naked_twin_pairs = [[twin, peer] for twin in naked_twin_list for peer in peers[twin] if values[twin] == values[peer]]
    naked_twin_pairs = set(tuple(sorted(permutation)) for permutation in naked_twin_pairs )
    
    for unit in unitlist:
        for twin1, twin2 in naked_twin_pairs:
            if twin1 in unit and twin2 in unit:
                for box in unit:
                    if twin1 != box and twin2 != box:
                        removal_characters = [removal_characters for removal_characters in values[twin1]]
                        for character in values[box]:
                            for duplicate in removal_characters:
                                if character == duplicate and len(values[box]) > 1:
                                    values[box] = values[box].replace(duplicate,'')

    return values


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    grid_dict = {}
    k = 0
    for box in boxes:
        value = '123456789'
        if grid[k] != '.':
            value = grid[k]
        assign_value(grid_dict, box, value)
        k += 1

    return grid_dict


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in columns))
        if r in 'CF': print(line)
    print


def eliminate(values):
    for box in boxes:
        if len(values[box]) == 1:
            for peer_boxes in peers[box]:
                values[peer_boxes] = values[peer_boxes].replace(values[box],'')
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))


# Initalize all the variables used for solving the sudoku puzzle.
rows = 'ABCDEFGHI'
columns = '123456789'
boxes = cross(rows, columns)
row_units = [ cross(rows, col) for col in columns ]
column_units = [ cross(row, columns) for row in rows ]
square_units = [ cross(c,r) for c in ('ABC','DEF','GHI') for r in ('123','456','789' )]
unitlist = column_units + row_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

# Create diagonal peers.
diagonal_boxes_negative_slope = [rows[k]+columns[k] for k in range(len(columns))]
diagonal_boxes_positive_slope = [rows[k]+columns[len(columns)-k-1] for k in range(len(columns))]

# Add new diagonal peers to peers dictionary.
for box in diagonal_boxes_negative_slope:
    diagonal_peers = set([new_box for new_box in diagonal_boxes_negative_slope if new_box not in peers[box]]) - set([box])
    peers[box] = peers[box].union(diagonal_peers)

for box in diagonal_boxes_positive_slope:
    diagonal_peers = set([new_box for new_box in diagonal_boxes_positive_slope if new_box not in peers[box]]) - set([box])
    peers[box] = peers[box].union(diagonal_peers)


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
