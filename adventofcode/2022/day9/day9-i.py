import math

with open('input.txt') as f:

    h_pos, t_pos = [0, 0], [0, 0]
    visited_pos = {f"{t_pos[0]}-{t_pos[1]}"}

    for l in f.readlines():
        l = l.rstrip()
        if len(l) == 0:
            continue

        d, s = l[0], int(l[1:])

        op = 1 if d == 'R' or d == 'U' else -1
        axis = 0 if d == 'R' or d == 'L' else 1

        for i in range(s):
            h_pos[axis] += 1 * op

            diff = [h_pos[0] - t_pos[0], h_pos[1] - t_pos[1]]

            if math.sqrt(diff[0]**2 + diff[1]**2) == 1 or \
                    (abs(diff[0]) == 1 and abs(diff[1]) == 1):
                continue

            if abs(diff[0]) == 2 and diff[1] == 0:
                t_pos[0] += (diff[0] + (1 if diff[0] < 0 else -1))
            elif diff[0] == 0 and abs(diff[1]) == 2:
                t_pos[1] += (diff[1] + (1 if diff[1] < 0 else -1))

            else:
                if abs(diff[0]) == 1:
                    t_pos[0] += diff[0]
                    t_pos[1] += (diff[1] + (1 if diff[1] < 0 else -1))
                elif abs(diff[1]) == 1:
                    t_pos[1] += diff[1]
                    t_pos[0] += (diff[0] + (1 if diff[0] < 0 else -1))

            visited_pos.add(f"{t_pos[0]}-{t_pos[1]}")

    print(h_pos, t_pos)
    print(len(visited_pos))