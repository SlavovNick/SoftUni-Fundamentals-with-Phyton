word = ""
while word != "End":
    for i in range(len(word)):
        if word == "SoftUni":
            break
        print(word[i], end='')
        if i == len(word) - 1:
            print(word[i])
        else:
            print(word[i], end='')
    word = input()