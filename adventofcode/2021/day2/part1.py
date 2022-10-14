commands = []
with open('input.txt') as f:
    commands = f.readlines()

horizontal_pos, depth = 0, 0

for command in commands:
    verb, value = command.split(' ')

    if verb == 'forward':
        horizontal_pos += int(value)
    elif verb == 'down':
        depth += int(value)
    else:
        depth -= int(value)

print(horizontal_pos * depth)



