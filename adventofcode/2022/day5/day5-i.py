with open('input.txt') as f:
    build_stack = True
    stack_lines = []
    stacks = None

    for line in f:
        line = line.rstrip()

        if len(line) == 0:
            build_stack = False
            stack_lines = stack_lines[::-1]

            count_stacks = int(stack_lines.pop(0)[-1])
            stacks = {i: [] for i in range(1, count_stacks + 1)}

            for stack_line in stack_lines:
                for i in stacks.keys():
                    if len(stack_line) - 1 >= 4 * i - 3:
                        container = stack_line[4 * i - 3].strip()
                        if len(container) > 0:
                            stacks[i].append(container)

            continue

        if build_stack:
            stack_lines.append(line)
            continue

        command = [int(x) for x in line.split(" ") if x.isdigit()]
        for i in range(command[0]):
            stacks[command[2]].append(stacks[command[1]].pop())

    print("".join([s[-1] for s in stacks.values()]))
