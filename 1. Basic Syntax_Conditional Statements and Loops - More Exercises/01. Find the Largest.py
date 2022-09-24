number = input()
bigest_number = ""

for i in range(len(number)):
    pos = 0
    max_digit = 0
    for j in range(len(number)):
        if number[j] != '*':
            n = int(number[j])
            if max_digit <= n:
                max_digit = n
                pos = j
    bigest_number = bigest_number + number[pos]
    number = number[:pos] + '*' + number[pos + 1:]

print(bigest_number)


