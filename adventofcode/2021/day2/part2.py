commands = []
with open('input.txt') as f:
    commands = f.readlines()

horizontal_pos, depth, aim = 0, 0, 0

for command in commands:
    verb, value = command.split(' ')

    if verb == 'forward':
        horizontal_pos += int(value)
        depth += aim * int(value)
    elif verb == 'down':
        aim += int(value)
    else:
        aim -= int(value)

print(horizontal_pos * depth)



