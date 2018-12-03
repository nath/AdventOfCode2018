from collections import defaultdict
import itertools
import re

with open("input.txt") as f:
    claims = [tuple(map(int, re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups())) for line in f]

fabric = defaultdict(int)

def positionsInClaim(claim):
    number, leftOffset, topOffset, width, height = claim
    xs = range(leftOffset, leftOffset + width)
    ys = range(topOffset, topOffset + height)

    return itertools.product(xs, ys)

for claim in claims:
    for position in positionsInClaim(claim):
        fabric[position] += 1

##########
# Part 1 #
##########

print("Part 1:", sum(numberOfClaims > 1 for numberOfClaims in fabric.values()))


##########
# Part 2 #
##########

for claim in claims:
    if all(fabric[position] == 1 for position in positionsInClaim(claim)):
        print("Part 2:", claim[0])
