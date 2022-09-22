string = input().split(', ')
sheep = 0
for i in range(len(string) - 1, -1, -1):
    if string[i] == "wolf":
        if i == len(string) - 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {sheep}! You are about to be eaten by a wolf!")
    sheep += 1
