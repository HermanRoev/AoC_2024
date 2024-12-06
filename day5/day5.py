import time

start = time.perf_counter()
with open('data.txt') as f:
    data = f.read().split('\n')

# Task 1
rules = [(int(line.split('|')[0]), int(line.split('|')[1])) for line in data if '|' in line]
updates = [[int(i) for i in line.split(',')] for line in data if ',' in line]

incorrect_updates = []
total_sum = 0
for update in updates:
    ordered = True
    for i in range(len(update)):
        number = update[i]
        if not ordered:
            break
        for before, after in rules:
            if not ordered:
                break
            if number not in [before, after]:
                continue
            if number == before:
                for j in range(i):
                    if update[i-j] == after:
                        ordered = False
            if number == after:
                for j in range(i, len(update)):
                    if update[j] == before:
                        ordered = False
    if ordered:
        total_sum += (update[len(update) // 2])
    if not ordered:
        incorrect_updates.append(update)

print(f'Total sum of all valid updates are {total_sum}')
middle_time = time.perf_counter()
print(f'Execution time: {middle_time - start}')

total_sum = 0
# Task 2
for update in incorrect_updates:
    made_changes = True
    while made_changes:
        made_changes = False
        for rule in rules:
            before, after = rule
            if before in update and after in update:
                before_index, after_index = update.index(before), update.index(after)
                if before_index > after_index:
                    update.pop(before_index)
                    update.insert(after_index, before)
                    made_changes = True

    total_sum += update[len(update) // 2]

print(f'Total sum of all invalid updates are {total_sum}')
print(f'Execution time: {time.perf_counter() - middle_time}')
