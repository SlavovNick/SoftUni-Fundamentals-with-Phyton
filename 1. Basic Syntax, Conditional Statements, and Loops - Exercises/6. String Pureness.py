n = int(input())

for _ in range(n):
    str = input()
    pure = True
    for i in range(len(str)):
        if str[i] == ',' or str[i] == '.' or str[i] == '_':
            pure = False

    if pure:
        print(f"{str} is pure.")
    else:
        print(f"{str} is not pure!")

