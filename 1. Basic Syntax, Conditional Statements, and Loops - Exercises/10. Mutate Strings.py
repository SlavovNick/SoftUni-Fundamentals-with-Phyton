one = input()
two = input()
three = ""
for i in range(len(one)):
    if one[i] != two[i]:
        three += two[i]
        four = three
        for j in range(i + 1, len(one)):
            three += one[j]
        print(three)
        three = four
    else:
        three += one[i]
