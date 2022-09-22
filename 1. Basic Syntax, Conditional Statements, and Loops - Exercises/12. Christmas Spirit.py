budget = 0
totalSpirit = 0
quantity = int(input())
days = int(input())
curr_day = 1

while curr_day < days + 1:
    if curr_day % 11 == 0:
        quantity += 2
    if curr_day % 2 == 0:
        budget += 2 * quantity
        totalSpirit += 5
    if curr_day % 3 == 0:
        budget += 8 * quantity
        totalSpirit += 13
    if curr_day % 5 == 0:
        budget += 15 * quantity
        totalSpirit += 17
        #if curr_day % 3 == 0:
            #totalSpirit += 30
    if curr_day % 10 == 0:
        budget += 23
        totalSpirit -= 20
    curr_day += 1
if curr_day == 10:
    totalSpirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
