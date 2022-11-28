def solve(right, down):
    with open('input.txt') as f:
        cur_row, cur_col, trees = 0, 0, 0

        for line in f:
            if cur_row % down != 0:
                cur_row += 1
                continue

            line = line.rstrip()
            if line[cur_col] == "#":
                trees += 1

            if cur_col + right > len(line) - 1:
                cur_col = right - (len(line) - 1 - cur_col) - 1
            else:
                cur_col += right

            cur_row += 1

        return trees


print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
