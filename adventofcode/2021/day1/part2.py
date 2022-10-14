file = open('input.txt', 'r')
lines = file.readlines()
file.close()

measurements = []
counter = 0

for x in range(0, len(lines)):
    if (x + 2) > (len(lines) - 1):
        continue

    measurements.append(int(lines[x]) + int(lines[x + 1]) + int(lines[x + 2]))
    if x != 0 and measurements[x] > measurements[x - 1]:
        counter += 1

print(counter)