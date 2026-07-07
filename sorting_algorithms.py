data = [8, 3, 1, 7, 0, 10, 2]

n = len(data)

for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print("Sorted data:", data)
