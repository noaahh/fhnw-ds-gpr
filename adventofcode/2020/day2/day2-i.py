def solve():
    with open('input.txt') as f:
        valid = 0
        for line in f:
            parts = line.rstrip().split(" ")
            limits = [int(x) for x in parts[0].split("-")]
            if limits[0] <= parts[-1].count(parts[1][0]) <= limits[1]:
                valid += 1

        return valid


print(solve())
