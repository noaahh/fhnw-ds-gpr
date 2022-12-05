with open('input.txt') as f:
    top_three = []
    running_sum = 0

    for line in f:
        line = line.rstrip()

        if len(line) == 0:
            if any(x < running_sum for x in top_three) and len(top_three) >= 3:
                top_three.remove(min(top_three))
                top_three.append(running_sum)
            elif len(top_three) < 3:
                top_three.append(running_sum)

            running_sum = 0
        else:
            running_sum += int(line)

    print(sum(top_three))
