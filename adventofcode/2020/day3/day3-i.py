def solve():
    with open('input.txt') as f:
        cur_col, trees = 0, 0

        for line in f:
            line = line.rstrip()
            if line[cur_col] == "#":
                trees += 1

            if cur_col + 3 > len(line) - 1:
                cur_col = 3 - (len(line) - 1 - cur_col) - 1
            else:
                cur_col += 3

        return trees


print(solve())
