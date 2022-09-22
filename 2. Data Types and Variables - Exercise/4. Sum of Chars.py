lines = int(input())
total_sum = 0
for i in range(1, lines + 1):
    total_sum += ord(input())

print(f"The sum equals: {total_sum}")