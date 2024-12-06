import copy
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

def find_start_position(map_data):
    """
    Finds the starting position in the map marked by one of the direction symbols.

    :param map_data: 2D list representing the map.
    :return: Tuple containing the direction symbol and its coordinates (direction, x, y).
    """
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] in '^>v<':
                return map_data[i][j], i, j
    return None, None, None  # If no starting position is found

def scan_ahead(map_data, direction, x, y):
    """
    Scans ahead in the given direction to find the next obstacle or boundary.

    :param map_data: 2D list representing the map.
    :param direction: Current direction ('^', '>', 'v', '<').
    :param x: Current row index.
    :param y: Current column index.
    :return: Tuple containing the new coordinates after scanning and a boolean indicating
             whether an obstacle was hit.
    """
    rows = len(map_data)
    cols = len(map_data[0]) if rows > 0 else 0
    hit_obstacle = False

    if direction == '^':
        new_x = x - 1
        while new_x >= 0 and map_data[new_x][y] != '#':
            new_x -= 1
        if new_x >= 0 and map_data[new_x][y] == '#':
            hit_obstacle = True
        else:
            new_x = -1  # Indicates boundary
        return new_x, y, hit_obstacle

    elif direction == '>':
        new_y = y + 1
        while new_y < cols and map_data[x][new_y] != '#':
            new_y += 1
        if new_y < cols and map_data[x][new_y] == '#':
            hit_obstacle = True
        else:
            new_y = cols  # Indicates boundary
        return x, new_y, hit_obstacle

    elif direction == 'v':
        new_x = x + 1
        while new_x < rows and map_data[new_x][y] != '#':
            new_x += 1
        if new_x < rows and map_data[new_x][y] == '#':
            hit_obstacle = True
        else:
            new_x = rows  # Indicates boundary
        return new_x, y, hit_obstacle

    elif direction == '<':
        new_y = y - 1
        while new_y >= 0 and map_data[x][new_y] != '#':
            new_y -= 1
        if new_y >= 0 and map_data[x][new_y] == '#':
            hit_obstacle = True
        else:
            new_y = -1  # Indicates boundary
        return x, new_y, hit_obstacle

def find_total_traversed(map_data):
    """
    Traverses the map from the starting position by scanning ahead until the next obstacle or boundary,
    marking traversed tiles, and collecting their coordinates.

    :param map_data: 2D list representing the map.
    :return: Tuple containing the total number of tiles crossed and a set of traversed cell coordinates.
    """
    data = copy.deepcopy(map_data)
    direction, x, y = find_start_position(data)

    if direction is None:
        raise ValueError("No starting position found in the map.")

    traversed_cells = set()

    while True:
        new_x, new_y, hit_obstacle = scan_ahead(data, direction, x, y)

        if hit_obstacle:
            # Traverse from (x, y) to (new_x, new_y) exclusive
            if direction == '^':
                for i in range(new_x + 1, x):
                    traversed_cells.add((i, y))
                    data[i][y] = 'X'
                direction = '>'  # Clockwise turn
                x = new_x + 1  # Move back to before the obstacle
            elif direction == '>':
                for j in range(y + 1, new_y):
                    traversed_cells.add((x, j))
                    data[x][j] = 'X'
                direction = 'v'  # Clockwise turn
                y = new_y - 1  # Move back to before the obstacle
            elif direction == 'v':
                for i in range(x + 1, new_x):
                    traversed_cells.add((i, y))
                    data[i][y] = 'X'
                direction = '<'  # Clockwise turn
                x = new_x - 1  # Move back to before the obstacle
            elif direction == '<':
                for j in range(new_y + 1, y):
                    traversed_cells.add((x, j))
                    data[x][j] = 'X'
                direction = '^'  # Clockwise turn
                y = new_y + 1  # Move back to before the obstacle
        else:
            # Traverse from (x, y) to the boundary
            if direction == '^':
                for i in range(new_x + 1, x):
                    traversed_cells.add((i, y))
                    data[i][y] = 'X'
                break  # Reached boundary
            elif direction == '>':
                for j in range(y + 1, new_y):
                    traversed_cells.add((x, j))
                    data[x][j] = 'X'
                break  # Reached boundary
            elif direction == 'v':
                for i in range(x + 1, new_x):
                    traversed_cells.add((i, y))
                    data[i][y] = 'X'
                break  # Reached boundary
            elif direction == '<':
                for j in range(new_y + 1, y):
                    traversed_cells.add((x, j))
                    data[x][j] = 'X'
                break  # Reached boundary

    # Count traversed tiles including the starting position
    total_sum = sum(
        1 for row in data for cell in row if cell in 'X^>v<'
    )

    return total_sum, traversed_cells

def traverse_map(map_data):
    """
    Traverses the map to detect if an infinite loop occurs by tracking visited states.
    Utilizes scan-ahead traversal.

    :param map_data: 2D list representing the map.
    :return: True if a cycle is detected, False otherwise.
    """
    direction, x, y = find_start_position(map_data)

    if direction is None:
        raise ValueError("No starting position found in the map.")

    visited_states = set()

    while True:
        state = (x, y, direction)
        if state in visited_states:
            # Cycle detected
            return True
        visited_states.add(state)

        new_x, new_y, hit_obstacle = scan_ahead(map_data, direction, x, y)

        if hit_obstacle:
            # Traverse from (x, y) to (new_x, new_y) exclusive
            if direction == '^':
                x = new_x + 1  # Move back to before the obstacle
                direction = '>'  # Clockwise turn
            elif direction == '>':
                y = new_y - 1  # Move back to before the obstacle
                direction = 'v'  # Clockwise turn
            elif direction == 'v':
                x = new_x - 1  # Move back to before the obstacle
                direction = '<'  # Clockwise turn
            elif direction == '<':
                y = new_y + 1  # Move back to before the obstacle
                direction = '^'  # Clockwise turn
        else:
            # Traverse from (x, y) to the boundary
            break  # No cycle detected, traversal ends

    return False  # No cycle detected

def check_cycle(map_data, i, j):
    """
    Checks if adding an obstacle '#' at position (i, j) causes a cycle in traversal.

    :param map_data: 2D list representing the original map.
    :param i: Row index where the obstacle is to be added.
    :param j: Column index where the obstacle is to be added.
    :return: True if a cycle is detected after adding the obstacle, False otherwise.
    """
    # Skip invalid positions
    if map_data[i][j] in ['#', '^', '>', 'v', '<']:
        return False

    # Create a deep copy of the map and add the obstacle
    modified_map = [row[:] for row in map_data]  # Faster than copy.deepcopy for 2D lists
    modified_map[i][j] = '#'

    # Check for a cycle
    has_cycle = traverse_map(modified_map)
    return has_cycle

def find_all_possible_loop_locations(map_data, traversed_cells):
    """
    Finds all positions where adding an obstacle '#' causes the traversal to enter an infinite loop.
    Utilizes multiprocessing to speed up the computation.

    :param map_data: 2D list representing the original map.
    :param traversed_cells: Set of tuples representing traversed cell coordinates.
    :return: Total number of positions that cause cycles when an obstacle is added.
    """
    total_sum = 0
    positions = list(traversed_cells)  # Only check traversed cells

    # Prepare arguments for multiprocessing
    args_list = [(map_data, i, j) for (i, j) in positions]

    # Use ProcessPoolExecutor for multiprocessing
    with ProcessPoolExecutor() as executor:
        # Submit all tasks to the executor
        futures = [executor.submit(check_cycle, *args) for args in args_list]

        # Use tqdm to display a progress bar
        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing Loop Locations"):
            try:
                if future.result():
                    total_sum += 1
            except Exception as e:
                # Handle exceptions if necessary
                print(f"Error processing position: {e}")

    return total_sum

def main():
    # Read the map from 'data.txt'
    with open('data.txt', 'r') as file:
        data = [list(line.rstrip('\n')) for line in file]

    # Calculate total number of tiles crossed and get traversed cells
    total_traversed, traversed_cells = find_total_traversed(data)
    print(f'Total number of tiles crossed: {total_traversed}')

    # Find all loop-causing obstacle positions using multiprocessing
    total_loop_locations = find_all_possible_loop_locations(data, traversed_cells)
    print(f'Total number of loop locations: {total_loop_locations}')

if __name__ == "__main__":
    main()
