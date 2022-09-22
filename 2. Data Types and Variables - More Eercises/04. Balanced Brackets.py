n = int(input())

left = 0
right = 0
st = True

for _ in range(n):
    line = input()

    if line == "(":
        left += 1
    if line == ")":
        if left == 1 and right == 0:
            left = 0
            right = 0
        else:
            right += 1

if left == 0 and right == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
