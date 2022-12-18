with open('input.txt') as f:
    grid = [l.rstrip() for l in f.readlines()]
    visible = (len(grid) - 2) * 2 + 2 * len(grid[0])

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            tree = int(grid[i][j])
            visible += 1 if all([int(grid[ti][j]) < tree for ti in range(i)]) or \
                            all([int(grid[ti][j]) < tree for ti in range(i + 1, len(grid))]) or \
                            all([int(grid[i][tj]) < tree for tj in range(j)]) or \
                            all([int(grid[i][tj]) < tree for tj in range(j + 1, len(grid[i]))]) else 0

    print(visible)