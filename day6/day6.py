import copy
from tqdm import tqdm

with open('data.txt', 'r') as file:
    data = [[i for i in line] for line in file.read().split('\n')]


def find_start_position(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in '^>v<':
                return map[i][j], i, j


def find_total_traversed(map):
    data = copy.deepcopy(map)
    direction, x, y = find_start_position(data)
    while True:
        if direction == '^':
            x -= 1
            if x < 0:
                break
            if data[x][y] == '#':
                direction = '>'
                x += 1
            else:
                data[x][y] = 'X'
        elif direction == '>':
            y += 1
            if y >= len(data[x]):
                break
            if data[x][y] == '#':
                direction = 'v'
                y -= 1
            else:
                data[x][y] = 'X'
        elif direction == 'v':
            x += 1
            if x >= len(data):
                break

            if data[x][y] == '#':
                direction = '<'
                x -= 1
            else:
                data[x][y] = 'X'
        elif direction == '<':
            y -= 1
            if y < 0:
                break
            if data[x][y] == '#':
                direction = '^'
                y += 1
            else:
                data[x][y] = 'X'


    total_sum = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in 'X^>v<':
                total_sum += 1

    return total_sum


def traverse_map(data):
    direction, x, y = find_start_position(data)

    visited_states = set()

    while True:
        state = (x, y, direction)
        if state in visited_states:
            return True
        visited_states.add(state)

        if direction == '^':
            x -= 1
            if x < 0:
                break
            if data[x][y] == '#':
                direction = '>'
                x += 1
        elif direction == '>':
            y += 1
            if y >= len(data[x]):
                break
            if data[x][y] == '#':
                direction = 'v'
                y -= 1
        elif direction == 'v':
            x += 1
            if x >= len(data):
                break
            if data[x][y] == '#':
                direction = '<'
                x -= 1
        elif direction == '<':
            y -= 1
            if y < 0:
                break
            if data[x][y] == '#':
                direction = '^'
                y += 1

    return False


def find_all_possible_loop_locations(data):
    total_sum = 0
    for i in tqdm(range(len(data))):
        for j in range(len(data[i])):
            current_cell = data[i][j]
            if current_cell in ['#', '^', '>', 'v', '<']:
                continue

            modified_map = copy.deepcopy(data)
            modified_map[i][j] = '#'

            has_cycle = traverse_map(modified_map)
            if has_cycle:
                total_sum += 1

    return total_sum


print(f'Total number of tiles crossed: {find_total_traversed(data)}')
print(f'Total number of loop locations: {find_all_possible_loop_locations(data)}')
