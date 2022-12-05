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
    for line in f:
        line = line.rstrip()

        compartment_border = int(len(line) / 2)
        compartments = [assign_letter_values(line[:compartment_border]),
                        assign_letter_values(line[compartment_border:])]

        item_sum += [c for c in compartments[0] if c in compartments[1]][0]

    print(item_sum)
