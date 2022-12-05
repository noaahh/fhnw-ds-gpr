with open('input.txt') as f:
    overlaps = 0
    for line in f:
        pair = []
        for elve in line.rstrip().split(","):
            elve_limits = []
            for limit in elve.split("-"):
                elve_limits.append(int(limit))

            pair.append(elve_limits)

        x, y = pair
        if x[0] <= y[0] <= x[1] or y[0] <= x[0] <= y[1]:
            overlaps += 1

    print(overlaps)
