# A for Rock, B for Paper, and C for Scissors
# X           Y                Z
moves_mapping = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

strikes = {
    "A": "C",
    "B": "A",
    "C": "B"
}

moves = {
    "A": 1,
    "B": 2,
    "C": 3
}

with open('input.txt') as f:
    score = 0

    for line in f:
        line = line.rstrip()
        opp, me = line.split(" ")
        me = moves_mapping[me]

        # shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
        # round (0 if you lost, 3 if the round was a draw, and 6 if you won)
        if strikes[opp] == me:
            score += moves[me]
        elif opp == me:
            score += 3 + moves[me]
        else:
            score += 6 + moves[me]

    print(score)
