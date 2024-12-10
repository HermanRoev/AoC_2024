from collections import defaultdict

with open('input.txt') as f:
    lines = f.readlines()
    map = [[char for char in x.strip()] for x in lines]

node_dict = defaultdict(list)
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '.':
            node_dict[map[i][j]].append((i, j))

max_x = len(map[0])
max_y = len(map)
min_x = 0
min_y = 0
for key in node_dict:
    for i in range(len(node_dict[key]) - 1):
        x, y = node_dict[key][i]
        for j in range(i + 1, len(node_dict[key])):
            x2, y2 = node_dict[key][j]
            diff_x, diff_y = x-x2, y-y2
            new_x, new_y = x + diff_x, y + diff_y
            new_x2, new_y2 = x2 - diff_x, y2 - diff_y
            # To solve part 1, change while loops with if and remove line 31 and 35
            while min_x <= new_x < max_x and min_y <= new_y < max_y:
                if map[new_x][new_y] != '#':
                    map[new_x][new_y] = '#'
                new_x, new_y = new_x + diff_x, new_y + diff_y
            while min_x <= new_x2 < max_x and min_y <= new_y2 < max_y:
                if map[new_x2][new_y2] != '#':
                    map[new_x2][new_y2] = '#'
                new_x2, new_y2 = new_x2 - diff_x, new_y2 - diff_y

total_count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '.': # Change this to '#' to solve part 1
            total_count += 1

print(total_count)