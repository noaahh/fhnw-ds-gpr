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

def get_range(interval):
    is_neg = interval < 0
    return range(0, interval, -1 if is_neg else 1)

for line in lines:
    x_interval = line[1][0] - line[0][0]
    y_interval = line[1][1] - line[0][1]

    points = []
    x,y = line[0]

    if y_interval == 0:
        for i in get_range(x_interval):
            points.append((x + i, y))
    elif x_interval == 0:
        for i in get_range(y_interval):
            points.append((x, y + i))
    else:
        is_synced = (line[1][0] > line[0][0] and line[1][1] > line[0][1]) or (line[1][0] < line[0][0] and line[1][1] < line[0][1])
        for i in get_range(x_interval):
            points.append((x + i, y + i * (1 if is_synced else -1)))
                

    points.append(line[1])
    for point in points:
        diagram[point[1]][point[0]] += 1


intersections = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        intersections += 1 if diagram[i][j] > 1 else 0

print(intersections)