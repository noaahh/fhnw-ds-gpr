with open('input.txt') as f:
    containing = 0
    for line in f:
        pair = []

        for elve in line.rstrip().split(","):
            elve_limits = []
            for limit in elve.split("-"):
                elve_limits.append(int(limit))

            pair.append(elve_limits)

        large = pair.pop(pair.index(max(pair, key=lambda x: x[1] - x[0])))
        small = pair[0]

        if large[0] <= small[0] and small[1] <= large[1]:
            containing += 1

    print(containing)