with open("Day 1/input.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]

elfs_calories = []
total = 0

for calories in lines:
    if calories != "":
        total += int(calories)
    else:
        elfs_calories.append(total)
        total = 0

print(max(elfs_calories))
