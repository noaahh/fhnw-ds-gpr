with open('input.txt') as f:
    grid = [l.rstrip() for l in f.readlines()]
    highest_score = 0

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            tree = int(grid[i][j])

            # Up
            distance_up = 0
            for ti in range(i - 1, -1, -1):
                distance_up += 1
                if int(grid[ti][j]) >= tree:
                    break

            # Down
            distance_down = 0
            for ti in range(i + 1, len(grid)):
                distance_down += 1
                if int(grid[ti][j]) >= tree:
                    break

            # Left
            distance_left = 0
            for tj in range(j - 1, -1, -1):
                distance_left += 1
                if int(grid[i][tj]) >= tree:
                    break

            # Right
            distance_right = 0
            for tj in range(j + 1, len(grid[i])):
                distance_right += 1
                if int(grid[i][tj]) >= tree:
                    break

            score = distance_right * distance_left * distance_up * distance_down
            if score > highest_score:
                highest_score = score


    print(highest_score)