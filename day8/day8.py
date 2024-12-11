from collections import defaultdict
import time
from copy import deepcopy

start = time.perf_counter()

with open('input.txt') as f:
    lines = f.readlines()
    org_map = [[char for char in x.strip()] for x in lines]

node_dict = defaultdict(list)
for i in range(len(org_map)):
    for j in range(len(org_map[i])):
        if org_map[i][j] != '.':
            node_dict[org_map[i][j]].append((i, j))

max_x = len(org_map[0])
max_y = len(org_map)
min_x = 0
min_y = 0

map1 = deepcopy(org_map)
map2 = deepcopy(org_map)

for key in node_dict:
    for i in range(len(node_dict[key]) - 1):
        x, y = node_dict[key][i]
        for j in range(i + 1, len(node_dict[key])):
            x2, y2 = node_dict[key][j]
            diff_x, diff_y = x - x2, y - y2
            new_x, new_y = x + diff_x, y + diff_y
            new_x2, new_y2 = x2 - diff_x, y2 - diff_y

            # Part 1
            if min_x <= new_x < max_x and min_y <= new_y < max_y:
                if map1[new_x][new_y] != '#':
                    map1[new_x][new_y] = '#'
            if min_x <= new_x2 < max_x and min_y <= new_y2 < max_y:
                if map1[new_x2][new_y2] != '#':
                    map1[new_x2][new_y2] = '#'

            # Part 2
            while min_x <= new_x < max_x and min_y <= new_y < max_y:
                if map2[new_x][new_y] != '#':
                    map2[new_x][new_y] = '#'
                new_x, new_y = new_x + diff_x, new_y + diff_y
            while min_x <= new_x2 < max_x and min_y <= new_y2 < max_y:
                if map2[new_x2][new_y2] != '#':
                    map2[new_x2][new_y2] = '#'
                new_x2, new_y2 = new_x2 - diff_x, new_y2 - diff_y

total_count1 = sum(row.count('#') for row in map1)
print(f"Part 1: {total_count1}")

total_count2 = sum(1 for row in map2 for cell in row if cell != '.')
print(f"Part 2: {total_count2}")

print(f"Time: {time.perf_counter() - start}")
