with open ('data.txt', 'r') as f:
    data = f.readlines()


def check_increasing(data):
    for i in range(len(data) - 1):
        number1 = data[i]
        number2 = data[i+1]
        if 3 >= number2 - number1 > 0:
            continue
        else:
            return 0
    return 1


def check_decreasing(data):
    for i in range(len(data) - 1):
        number1 = data[i]
        number2 = data[i+1]
        if 3 >= number1 - number2 > 0:
            continue
        else:
            return 0
    return 1


total = 0
for line in data:
    numbers = [int(x) for x in line.split(' ')]
    if check_increasing(numbers) or check_decreasing(numbers):
        total += 1
        continue
    for i in range(len(numbers)):
        testdata = numbers.copy()
        testdata.pop(i)
        if check_increasing(testdata) or check_decreasing(testdata):
            total += 1
            break

print(total)
