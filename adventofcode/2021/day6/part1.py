states = []
with open('input.txt') as file:
    states = list(map(int, file.readline().strip().split(',')))

for i in range(0, 80):
    day_states_len = len(states)
    for j in range(0, day_states_len):
        if states[j] == 0:
            states[j] = 6
            states.append(8)
        else:
            states[j] -= 1

print(len(states))