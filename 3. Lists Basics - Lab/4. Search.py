n = int(input())
word = input()
words = []

for _ in range(n):
    current_word = input()
    words.append(current_word)

print(words)


for i in range(len(words) - 1, -1, -1):
    if word not in words[i]:
        words.remove(words[i])

print(words)

