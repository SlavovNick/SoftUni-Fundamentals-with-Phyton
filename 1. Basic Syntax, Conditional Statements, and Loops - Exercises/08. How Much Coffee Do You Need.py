event = ""
coffie = 0
while event != "END":
    if event in ("coding", "dog", "cat", "movie"):
        coffie += 1
    elif event in ("CODING", "DOG", "CAT", "MOVIE"):
        coffie += 2
    event = input()

if coffie > 5:
    print("You need extra sleep")
else:
    print(coffie)