string = input()
temp = ""
indexes = []
for i in range(len(string)):
    temp = string[i]
    if temp.isupper():
        indexes.append(i)
    t=""
print(indexes)