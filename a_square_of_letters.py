LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))
chars = LETTERS[:layers][::-1]
indexes = list(range(1, layers + 1))
indexes += indexes[::-1][1:]

for i in indexes:
    line = chars[:i]
    line += line[-1] * (layers - len(line))
    line += line[::-1][1:]
    print(line)