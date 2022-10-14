file = open('input.txt', 'r')
lines = file.readlines()
file.close()

counter = 0

for x in range(0, len(lines)):
    if x == 0:
        continue

    if int(lines[x]) > int(lines[x - 1]):
        counter += 1

print(counter)