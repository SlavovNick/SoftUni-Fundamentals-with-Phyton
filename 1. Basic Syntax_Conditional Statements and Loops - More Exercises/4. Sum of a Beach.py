s = input()
beach_sum = 0
t = s.upper()
pos_1 = t.find("SAND")
pos_2 = t.find("WATER")
pos_3 = t.find("FISH")
pos_4 = t.find("SUN")
while pos_1 != -1 or pos_2 != -1 or pos_3 != -1 or pos_4 != -1:
    pos_1 = t.find("SAND")
    pos_2 = t.find("WATER")
    pos_3 = t.find("FISH")
    pos_4 = t.find("SUN")
    if pos_1 != -1:
        t = t[:pos_1] + '*' + t[pos_1 + 1:]
        beach_sum += 1
        continue
    if pos_2 != -1:
        t = t[:pos_2] + '*' + t[pos_2 + 1:]
        beach_sum += 1
        continue
    if pos_3 != -1:
        t = t[:pos_3] + '*' + t[pos_3 + 1:]
        beach_sum += 1
        continue
    if pos_4 != -1:
        t = t[:pos_4] + '*' + t[pos_4 + 1:]
        beach_sum += 1
        continue
print(beach_sum)