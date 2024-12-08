from tqdm import tqdm

with open('input.txt') as f:
    input = f.readlines()

data = []
for line in input:
    answer, values = line.split(':')
    values = [int(value) for value in values.strip().split(' ')]
    data.append((int(answer), values))

# Part 1... This was not funny!!!
total_sum = 0
for i in range(len(data)):
    answer, values = data[i]
    operator_spots = len(values) - 1
    total_combinations = 2 ** operator_spots
    for j in range(total_combinations):
        result = values[0]
        binary = bin(j)[2:].zfill(operator_spots)
        for k in range(len(values) - 1):
            if binary[k] == '0':
                result += values[k + 1]
            else:
                result *= values[k + 1]
        if result == answer:
            total_sum += answer
            break


print(f'The sum of the answers is {total_sum}')


# Part 2
total_sum = 0
for i in tqdm(range(len(data))):
    answer, values = data[i]
    operator_spots = len(values) - 1
    total_combinations = 3 ** operator_spots
    for j in range(total_combinations):
        result = values[0]
        digits = []
        while j > 0:
            digits.append(str(j % 3))
            j = j // 3

        ternary = ''.join(reversed(digits)).zfill(operator_spots)

        for k in range(len(values) - 1):
            if ternary[k] == '0':
                result += values[k + 1]
            elif ternary[k] == '1':
                result *= values[k + 1]
            elif ternary[k] == '2':
                result = int(str(result) + str(values[k + 1]))
        if result == answer:
            total_sum += answer
            break

print(f'The sum of the answers is {total_sum}')
