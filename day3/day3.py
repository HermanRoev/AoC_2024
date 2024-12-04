import re
import time

start = time.perf_counter()
with open("data.txt", "r") as file:
    corrupted_memory = file.read()


def extract_and_compute_sum(corrupted_memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, corrupted_memory)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total


print(extract_and_compute_sum(corrupted_memory))


def extract_and_compute_sum_with_conditions(corrupted_memory):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    condition_pattern = r"(do\(\)|don't\(\))"

    combined_pattern = re.compile(f"{mul_pattern}|{condition_pattern}")

    matches = combined_pattern.finditer(corrupted_memory)

    total = 0
    enabled = True

    for match in matches:
        if match.group(1) and match.group(2):
            if enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
        elif match.group(3):
            if match.group(3) == "do()":
                enabled = True
            elif match.group(3) == "don't()":
                enabled = False

    return total


print(extract_and_compute_sum_with_conditions(corrupted_memory))
print (f"Time taken: {time.perf_counter()-start}")