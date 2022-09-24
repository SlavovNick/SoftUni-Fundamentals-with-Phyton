key = int(input())
n = int(input())

message = ""

for i in range(n):
    letter = input()
    code = ord(letter) + key
    message = message + chr(code)

print(message)
