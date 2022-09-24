positive = []
negative = []
count_positives = 0
sum_of_negatives = 0

n = int(input())

for _ in range(n):
    c_num = int(input())
    if c_num >= 0:
        positive.append(c_num)
        count_positives += 1
    else:
        negative.append(c_num)
        sum_of_negatives += c_num

print(positive)
print(negative)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")