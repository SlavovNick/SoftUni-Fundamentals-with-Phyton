divisor = int(input())
boundary = int(input())

num = 1

for n in range(boundary + 1):
    if n % divisor == 0:
        num = n

print(num)