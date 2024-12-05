with open('data.txt') as f:
    grid = f.read().split('\n')

# Task 1
target_word = "XMAS"
reverse_word = target_word[::-1]

total_count = 0

grid_matrix = [list(row) for row in grid]
n_rows = len(grid_matrix)
n_cols = len(grid_matrix[0]) if n_rows > 0 else 0

for row in grid_matrix:
    line = ''.join(row)
    total_count += line.count(target_word) + line.count(reverse_word)

for c in range(n_cols):
    line = ''.join(grid_matrix[r][c] for r in range(n_rows))
    total_count += line.count(target_word) + line.count(reverse_word)

for c in range(n_cols):
    diagonal = []
    row, col = 0, c
    while row < n_rows and col < n_cols:
        diagonal.append(grid_matrix[row][col])
        row += 1
        col += 1
    if len(diagonal) >= 4:
        line = ''.join(diagonal)
        total_count += line.count(target_word) + line.count(reverse_word)

for r in range(1, n_rows):
    diagonal = []
    row, col = r, 0
    while row < n_rows and col < n_cols:
        diagonal.append(grid_matrix[row][col])
        row += 1
        col += 1
    if len(diagonal) >= 4:
        line = ''.join(diagonal)
        total_count += line.count(target_word) + line.count(reverse_word)

for c in range(n_cols - 1, -1, -1):
    diagonal = []
    row, col = 0, c
    while row < n_rows and col >= 0:
        diagonal.append(grid_matrix[row][col])
        row += 1
        col -= 1
    if len(diagonal) >= 4:
        line = ''.join(diagonal)
        total_count += line.count(target_word) + line.count(reverse_word)

for r in range(1, n_rows):
    diagonal = []
    row, col = r, n_cols - 1
    while row < n_rows and col >= 0:
        diagonal.append(grid_matrix[row][col])
        row += 1
        col -= 1
    if len(diagonal) >= 4:
        line = ''.join(diagonal)
        total_count += line.count(target_word) + line.count(reverse_word)

print(f'The word "XMAS" appears {total_count} times in the grid.')


#Task 2
count = 0
for i in range(1, n_rows-1):
    for j in range(1, n_cols-1):
        if grid_matrix[i][j] == 'A':
            # (TOP LEFT, BOTTOM RIGHT), (TOP RIGHT, BOTTOM LEFT)
            #MAS MAS
            if grid_matrix[i-1][j-1] == 'M' and grid_matrix[i+1][j+1] == 'S' and grid_matrix[i-1][j+1] == 'M' and grid_matrix[i+1][j-1] == 'S':
                count += 1
            #SAM SAM
            elif grid_matrix[i-1][j-1] == 'S' and grid_matrix[i+1][j+1] == 'M' and grid_matrix[i-1][j+1] == 'S' and grid_matrix[i+1][j-1] == 'M':
                count += 1
            #MAS SAM
            elif grid_matrix[i-1][j-1] == 'M' and grid_matrix[i+1][j+1] == 'S' and grid_matrix[i-1][j+1] == 'S' and grid_matrix[i+1][j-1] == 'M':
                count += 1
            #SAM MAS
            elif grid_matrix[i-1][j-1] == 'S' and grid_matrix[i+1][j+1] == 'M' and grid_matrix[i-1][j+1] == 'M' and grid_matrix[i+1][j-1] == 'S':
                count += 1

print(f'The word "MAS" in an X appears {count} times in the grid.')
























