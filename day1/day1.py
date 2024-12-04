def read_data(file_path):
    list1 = []
    list2 = []
    with open(file_path, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return sorted(list1), sorted(list2)


list1, list2 = read_data("data.txt")

total = 0
for i in range(len(list1)):
    # Find difference between two numbers at index i
    diff = abs(list2[i] - list1[i])
    # Add difference to total
    total += diff

print(total)

total = 0
for i in list1:
    counter = 0
    for j in range(len(list2)):
        if list2[j] == i:
            counter += 1
    total += i*counter

print(total)
