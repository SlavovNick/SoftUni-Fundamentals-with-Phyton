n = int(input())

max_value = 0
max_weight = 0
max_time = 0
max_quality = 0

for i in range(n):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight // snowball_time) ** snowball_quality
    if max_value <= snowball_value:
        max_weight = snowball_weight
        max_time = snowball_time
        max_value = snowball_value
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")