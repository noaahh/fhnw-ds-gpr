def solve():
    with open('input.txt') as f:
        valid = 0
        for line in f:
            parts = line.rstrip().split(" ")
            positions = [int(x) - 1 for x in parts[0].split("-")]

            l = parts[1][0]
            pwd = parts[-1]

            valid += sum(1 for i in range(2) if pwd[positions[i]] == l) % 2

        return valid


print(solve())
