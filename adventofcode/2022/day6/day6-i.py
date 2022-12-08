with open('input.txt') as f:
    for line in f:
        line = line.rstrip()

        for i in range(0, len(line)):
            if i < 3:
                continue

            chars = {}
            for c in line[i - 3:i + 1]:
                if c not in chars.keys():
                    chars[c] = 1
                else:
                    chars[c] += 1

            if sum(chars.values()) == len(chars.keys()):
                print(i + 1)
                break