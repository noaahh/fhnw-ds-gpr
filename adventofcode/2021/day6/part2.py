fish = {i: 0 for i in range(9)}

with open('input.txt') as file:
    for value in file.readline().strip().split(','):
        fish[int(value)] += 1
    
for day in range(256):
    zero_fish = fish[0]
    for i in range(1, 9):
        fish[i - 1] = fish[i]

    fish[8] = zero_fish
    fish[6] += zero_fish

print(sum(fish.values()))