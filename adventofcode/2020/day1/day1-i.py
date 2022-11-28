with open('input.txt') as f:
    prev_nums = []
    done = False

    for line in f:
        number = int(line.rstrip())

        for pn in prev_nums:
            if pn + number == 2020:
                print(number * pn)
                done = True
                break

        if done:
            break

        prev_nums.append(number)
