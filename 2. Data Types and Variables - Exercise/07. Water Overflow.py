n = int(input())
total_litres = 0

for i in range(n):
    litres = int(input())
    if total_litres + litres <= 255:
        total_litres += litres
    else:
            print("Insufficient capacity!")

print(total_litres)