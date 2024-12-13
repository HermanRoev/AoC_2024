from collections import deque

with open('input.txt') as f:
    input = f.read().split('\n')

map = [[char for char in line] for line in input]

# Part 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
checked_tiles = set()
tiles_to_check = deque()

total_score = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        edge_score = 0
        size = 0
        if (i, j) in checked_tiles:
            continue
        current_tile = map[i][j]
        tiles_to_check.append((i, j))
        checked_tiles.add((i, j))
        while tiles_to_check:
            tile = tiles_to_check.pop()
            size += 1
            for direction in directions:
                new_tile = (tile[0] + direction[0], tile[1] + direction[1])
                if (new_tile[0] < 0 or new_tile[0] >= len(map)
                        or new_tile[1] < 0 or new_tile[1] >= len(map[0])
                        or map[new_tile[0]][new_tile[1]] != current_tile):
                    edge_score += 1
                    continue
                if map[new_tile[0]][new_tile[1]] == current_tile and new_tile not in checked_tiles:
                    tiles_to_check.append(new_tile)
                    checked_tiles.add(new_tile)

        total_score += edge_score * size

print(f'The total score is {total_score}')

# Part 2
checked_tiles = set()
tiles_to_check = deque()

total_score = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) in checked_tiles:
            continue
        current_tile = map[i][j]
        tiles_to_check.append((i, j))
        checked_tiles.add((i, j))

        size = 0

        up = []
        down = []
        left = []
        right = []

        while tiles_to_check:
            tile = tiles_to_check.pop()
            tile_row, tile_column = tile
            size += 1
            for direction in directions:
                neighbor_row = tile_row + direction[0]
                neighbor_column = tile_column + direction[1]

                if (neighbor_row < 0 or neighbor_row >= len(map) or
                        neighbor_column < 0 or neighbor_column >= len(map[0]) or
                        map[neighbor_row][neighbor_column] != current_tile):

                    if direction == (0, 1):
                        right.append((tile_row, tile_column))
                    elif direction == (0, -1):
                        left.append((tile_row, tile_column))
                    elif direction == (1, 0):
                        down.append((tile_row, tile_column))
                    elif direction == (-1, 0):
                        up.append((tile_row, tile_column))
                    continue

                elif (neighbor_row, neighbor_column) not in checked_tiles:
                    tiles_to_check.append((neighbor_row, neighbor_column))
                    checked_tiles.add((neighbor_row, neighbor_column))

        up = sorted(up, key=lambda coord: (coord[0], coord[1]))
        down = sorted(down, key=lambda coord: (coord[0], coord[1]))
        left = sorted(left, key=lambda coord: (coord[1], coord[0]))
        right = sorted(right, key=lambda coord: (coord[1], coord[0]))

        side_coords = [(up, 'row'), (down, 'row'), (left, 'col'), (right, 'col')]

        sides = 0
        for sorted_list, axis in side_coords:
            previous = None
            for coord in sorted_list:
                if previous is None:
                    sides += 1
                else:
                    if axis == 'row':
                        if coord[0] != previous[0]:
                            sides += 1
                        elif coord[1] != previous[1] + 1:
                            sides += 1
                    elif axis == 'col':
                        if coord[1] != previous[1]:
                            sides += 1
                        elif coord[0] != previous[0] + 1:
                            sides += 1
                previous = coord

        total_score += sides * size

print(f'The total score is {total_score}')
