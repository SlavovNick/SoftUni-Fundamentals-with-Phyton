n = int(input())
str = ""
for i in range(n):
    str = "*"
    for j in range(i):
       str = str + "*"
    print(str)
for i in range(n - 1, 0, -1):
    str = ""
    for j in range(i, 0, -1):
        str = str + "*"
    print(str)