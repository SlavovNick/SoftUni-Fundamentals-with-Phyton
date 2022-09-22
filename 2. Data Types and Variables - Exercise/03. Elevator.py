import math
people = int(input())
capacity = int(input())

course = math.ceil(people / capacity)

print(course)