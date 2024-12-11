from collections import Counter
import time

start = time.perf_counter()

with open('input.txt', 'r') as file:
    data = file.read()

data = data.split(' ')
data = [int(i) for i in data]

stones = Counter(data)

for i in range(75):
    if i == 25:
        print(f'Part 1: {sum(stones.values())}')
    next_stones = Counter()
    for number, count in stones.items():
        if number == 0:
            next_stones[1] += count
        elif len(str(number)) % 2 == 0:
            half = len(str(number)) // 2
            left = int(str(number)[:half])
            right = int(str(number)[half:])
            next_stones[left] += count
            next_stones[right] += count
        else:
            next_stones[number * 2024] += count
    stones = next_stones

print(f'Part 2: {sum(stones.values())}')
print(f'Time: {time.perf_counter() - start}')
