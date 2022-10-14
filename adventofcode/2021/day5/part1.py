lines = []
with open('input.txt') as file:
    line = file.readline().strip()
    while line:
        cords = []
        for point in line.split('->'):
            point_split = list(map(int, point.split(',')))
            cords.append((point_split[0], point_split[1]))

        lines.append(cords)
        line = file.readline().strip()

dimension = (1000, 1000)
diagram = [[0 for j in range(0, dimension[0])] for i in range(0, dimension[1])]

for line in lines:
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        continue

    moving_index = 1 if line[0][0] == line[1][0] else 0
    distance = line[1][moving_index] - line[0][moving_index]

    is_negative = distance < 0
    distance += -1 if is_negative else 1

    for i in range(0, distance, -1 if is_negative else 1):
        x,y = 0,0
        if moving_index == 0:
            x = line[0][0] + i
            y = line[0][1]
        else:
            y = line[0][1] + i
            x = line[0][0]

        diagram[y][x] += 1


intersections = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        intersections += 1 if diagram[i][j] > 1 else 0

print(intersections)