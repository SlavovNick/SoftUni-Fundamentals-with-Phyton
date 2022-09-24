n = int(input())

for _ in range(n):
    mes = int(input())
    if mes == 88:
        print("Hello")
    elif mes == 86:
        print("How are you?")
    elif mes < 88:
        print("GREAT!")
    else:
        print("Bye.")