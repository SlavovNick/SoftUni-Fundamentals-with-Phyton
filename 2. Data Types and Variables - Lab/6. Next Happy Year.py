year = int(input())

while True:
    digits = 10 * [0]
    count_digit = 10 * [0]
    t_year = year
    count = 0

    while True:
        digit = t_year % 10
        digits[count] = digit
        t_year = (t_year - digit) // 10
        count += 1
        if t_year - digit == 0:
            break
    for i in range(count - 1):
        count_digit[digits[i]] += 1
    for i in range(10):
        if count_digit[i] > 1:
            happy_year = False
            break
        else:
            happy_year = True
    if happy_year:
        print(year)
        break
    year += 1




