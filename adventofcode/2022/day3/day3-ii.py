def assign_letter_values(string):
    letter_values = []
    for letter in string:
        if letter.islower():
            letter_values.append(ord(letter) - 96)
        else:
            letter_values.append(ord(letter) - 38)
    return letter_values


with open('input.txt') as f:
    item_sum = 0
    i = 1
    group_backpacks = []

    for line in f:
        line = line.rstrip()
        group_backpacks.append(assign_letter_values(line))

        if i == 3:
            item_sum += [x for x in group_backpacks[0] if x in group_backpacks[1] and x in group_backpacks[2]][0]

            i = 1
            group_backpacks = []
        else:
            i += 1

    print(item_sum)
