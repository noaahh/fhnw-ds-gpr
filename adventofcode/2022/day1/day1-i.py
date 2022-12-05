with open('input.txt') as f:
    loader_elf = 0
    running_sum = 0

    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            loader_elf = running_sum if running_sum > loader_elf else loader_elf
            running_sum = 0
        else:
            running_sum += int(line)

    print(loader_elf)