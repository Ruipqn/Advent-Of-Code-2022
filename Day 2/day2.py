with open("Day 2/input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]


"""
Opponent Hand:
    A = rock 
    B = paper
    C = scissors 
    
Part 1:
    X = rock 
    Y = paper
    Z = scissors 

Part 2:
    X = need to lose 
    Y = need to draw
    Z = need to win 
"""


def rps_p1(opponent, me):

    if opponent == "A":
        if me == "X":
            score = 4  # 1 rock + 3 draw

        elif me == "Y":
            score = 8  # 2 paper + 6 win

        elif me == "Z":
            score = 3  # 3 paper + 0 lost

        else:
            score = 0  # error

    elif opponent == "B":
        if me == "X":
            score = 1  # 1 rock + 0 lost

        elif me == "Y":
            score = 5  # 2 paper + 3 draw

        elif me == "Z":
            score = 9  # 3 paper + 6 win

        else:
            score = 0  # error

    elif opponent == "C":
        if me == "X":
            score = 7  # 1 rock + 6 win

        elif me == "Y":
            score = 2  # 2 paper + 0 lost

        elif me == "Z":
            score = 6  # 3 paper + 3 draw

        else:
            score = 0  # error

    else:
        score = 0  # error

    return score


def rps_p2(opponent, me):

    if opponent == "A":
        if me == "X":
            score = 3

        elif me == "Y":
            score = 4

        elif me == "Z":
            score = 8

        else:
            score = 0  # error

    elif opponent == "B":
        if me == "X":
            score = 1

        elif me == "Y":
            score = 5

        elif me == "Z":
            score = 9

        else:
            score = 0  # error

    elif opponent == "C":
        if me == "X":
            score = 2

        elif me == "Y":
            score = 6

        elif me == "Z":
            score = 7

        else:
            score = 0  # error

    else:
        score = 0  # error

    return score


total_score_p1, total_score_p2 = 0, 0

for hand in lines:
    game = hand.split()
    score_p1 = rps_p1(game[0], game[1])
    score_p2 = rps_p2(game[0], game[1])
    total_score_p1 += score_p1
    total_score_p2 += score_p2

print("Total score part 1 =", total_score_p1)
print("Total score part 2 =", total_score_p2)
