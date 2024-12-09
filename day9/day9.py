from tqdm import tqdm

with open('input.txt') as f:
    input = f.read()
    input = [int(x) for x in input]


# Part 1
def parse_input(input):
    output = []
    temp = 0
    for i in range(len(input)):
        if i % 2 == 0:
            for j in range(input[i]):
                output.append(temp)
        else:
            for j in range(input[i]):
                output.append('.')
            temp += 1
    return output


def sort(input):
    for i in tqdm(range(len(input))):
        if input[i] == '.':
            for j in range(len(input)):
                if j+i == len(input) - 1:
                    break
                if input[-j-1] != '.':
                    input[i], input[-j-1] = input[-j-1], input[i]
                    break

    return input


def get_total_score(input):
    total = 0
    for i in range(len(input)):
        if input[i] != '.':
            total += input[i]*i
    return total


# Part 2
def new_sort(input):
    current_type = '.'
    for i in tqdm(range(len(input))):
        count = 0
        if input[-i - 1] == current_type:
            continue
        if input[-i-1] != '.':
            current_type = input[-i-1]
            for j in range(10):
                if j+i == len(input) - 1:
                    break
                if input[-i-1-j] == current_type:
                    count += 1
                else:
                    break
            for k in range(len(input)):
                if k+i == len(input) - 1:
                    break
                if input[k] == '.':
                    valid = True
                    for l in range(count):
                        if input[k+l] != '.' or k+l == len(input) - 1:
                            valid = False
                            break
                    if valid:
                        for l in range(count):
                            input[k+l], input[-i-1-l] = input[-i-1-l], input[k+l]
                        break

    return input


print(f'Total score for part 1: {get_total_score(sort(parse_input(input)))}')
print(f'Total score for part 2: {get_total_score(new_sort(parse_input(input)))}')
