from collections import defaultdict
import re

with open("input.txt") as f:
    claims = [tuple(map(int, re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())) for line in f]

fabric = defaultdict(int)

##########
# Part 1 #
##########

overlaps = 0

for claim in claims:
    number, leftOffset, topOffset, width, height = claim
    for i in range(width):
        for j in range(height):
            position = (leftOffset + i, topOffset + j)
            fabric[position] += 1

            # only count the first time there's an overlapping claim
            if fabric[position] == 2:
                overlaps += 1

print("Part 1:", overlaps)


##########
# Part 2 #
##########

for claim in claims:
    number, leftOffset, topOffset, width, height = claim

    noneOverlap = True

    for i in range(width):
        for j in range(height):
            position = (leftOffset + i, topOffset + j)
            if fabric[position] > 1:
                noneOverlap = False

    if noneOverlap:
        print("Part 2:", number)
