# A for Rock, B for Paper, and C for Scissors

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

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

        if me == "X":
            score += moves[strikes[opp]]
        elif me == "Y":
            score += 3 + moves[opp]
        else:
            score += 6 + moves[list(strikes.keys())[list(strikes.values()).index(opp)]]

    print(score)
