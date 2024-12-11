from collections import deque
import time

start = time.perf_counter()

with open('input.txt') as f:
    input = f.read().splitlines()
    map = [[int(i) for i in row] for row in input]


# Part 1
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
deque = deque()

total_sum = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            end_nodes = set()
            deque.append((0, i, j))
            while deque:
                current_node, x, y = deque.popleft()
                for direction in directions:
                    next_x, next_y = x + direction[0], y + direction[1]
                    if 0 <= next_x < len(map) and 0 <= next_y < len(map[0]):
                        if map[next_x][next_y] == 9 and (next_x, next_y) in end_nodes:
                            continue
                        if map[next_x][next_y] == 9 and current_node + 1 == 9:
                            end_nodes.add((next_x, next_y))
                            total_sum += 1
                        if 9 != map[next_x][next_y] == current_node + 1:
                            deque.append((current_node + 1, next_x, next_y))

print(f'Total number trail ends reachable: {total_sum}')

total_sum = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            deque.append((0, i, j))
            while deque:
                current_node, x, y = deque.popleft()
                for direction in directions:
                    next_x, next_y = x + direction[0], y + direction[1]
                    if 0 <= next_x < len(map) and 0 <= next_y < len(map[0]):
                        if map[next_x][next_y] == 9 and current_node + 1 == 9:
                            total_sum += 1
                        if 9 != map[next_x][next_y] == current_node + 1:
                            deque.append((current_node + 1, next_x, next_y))

print(f'Total sum for all trail possibilities: {total_sum}')
print(f'Execution time: {time.perf_counter() - start}')
