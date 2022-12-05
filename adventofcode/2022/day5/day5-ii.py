with open('input.txt') as f:
    build_stack = True
    stacks = {}

    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            continue

        if build_stack and line.replace(" ", "").isdigit():
            for k in stacks.keys():
                stacks[k] = stacks[k][::-1]

            build_stack = False
            continue

        if build_stack:
            index, i = 1, 1
            while index <= len(line) - 1:
                if i not in stacks.keys():
                    stacks[i] = []

                container = line[index].strip()
                if len(container) == 1:
                    stacks[i].append(container)

                i += 1
                index = 4 * i - 3

            continue

        command = [int(x) for x in line.split(" ") if x.isdigit()]
        stacks[command[2]].extend([stacks[command[1]].pop() for _ in range(command[0])][::-1])

    print("".join([s[-1] for s in stacks.values()]))
