def solve():
    with open('input.txt') as f:
        prev_nums = []

        for line in f:
            number = int(line.rstrip())

            for i in range(len(prev_nums)):
                for j in range(1, len(prev_nums)):
                    if number + prev_nums[i] + prev_nums[j] == 2020:
                        return number * prev_nums[i] * prev_nums[j]

            prev_nums.append(number)


print(solve())
