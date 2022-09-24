numbers = []
filtered = []

n = int(input())

for _ in range(n):
    num = int(input())
    numbers.append(num)

command = input()

for i in range(n):
    if command == "even" and numbers[i] % 2 == 0:
        filtered.append(numbers[i])
    elif command == "odd" and numbers[i] % 2 == 1:
        filtered.append(numbers[i])
    elif command == "positive" and numbers[i] >= 0:
        filtered.append(numbers[i])
    elif command == "negative" and numbers[i] < 0:
        filtered.append(numbers[i])

print(filtered)
