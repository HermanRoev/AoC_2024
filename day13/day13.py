import re
import numpy as np

with open('input.txt') as f:
    data = f.read()

pattern = re.compile(r'X[+=](\d+), Y[+=](\d+)')
result = [tuple(tuple(map(int, match)) for match in pattern.findall(block))
          for block in data.strip().split('\n\n') if len(pattern.findall(block)) == 3]

score = 0
tolerance = 1e-3
offset = 10000000000000

# Part 1 and Part 2, just remove offset
for idx, equation in enumerate(result, 1):
    (a_x, a_y), (b_x, b_y), (prize_x, prize_y) = equation

    prize_x += offset
    prize_y += offset

    coefficients = np.array([[a_x, b_x], [a_y, b_y]])
    rhs = np.array([prize_x, prize_y])

    try:
        solution = np.linalg.solve(coefficients, rhs)
        a, b = solution

        if (abs(a - round(a)) < tolerance) and (abs(b - round(b)) < tolerance):
            a_rounded = int(round(a))
            b_rounded = int(round(b))
            score += a_rounded * 3 + b_rounded
    except np.linalg.LinAlgError:
        continue

print(f"\nTotal Score: {score}")
