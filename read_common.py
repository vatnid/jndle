chars = []

with open("test.txt", "r") as f:
    for line in f:
        line = line.strip()
        chars.extend(list(line))

print(chars)
print(len(chars))

