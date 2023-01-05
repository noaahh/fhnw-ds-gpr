import math

with open('input.txt') as f:
    knots = [[0, 0] for _ in range(10)]
    lead, tail = knots[0], knots[-1]

    visited_pos_tail = {f"{tail[0]}-{tail[1]}"}

    for l in f:
        l = l.rstrip()
        if len(l) == 0:
            continue

        d, s = l[0], int(l[2:])
        op = 1 if d == 'R' or d == 'U' else -1
        axis = 0 if d == 'R' or d == 'L' else 1

        for i in range(s):
            lead[axis] += 1 * op

            for ki in range(len(knots) - 1):
                h_pos, t_pos = knots[ki], knots[ki + 1]

                diff = [h_pos[0] - t_pos[0], h_pos[1] - t_pos[1]]

                if math.sqrt(diff[0]**2 + diff[1]**2) == 1 or \
                        (abs(diff[0]) == 1 and abs(diff[1]) == 1) or \
                        sum(diff) == 0:
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

                if t_pos == tail:
                    visited_pos_tail.add(f"{t_pos[0]}-{t_pos[1]}")

    print(knots)
    print(visited_pos_tail)
    print(len(visited_pos_tail))