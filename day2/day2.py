with open('input.txt') as f:
    lines = [line for line in f]

##########
# Part 1 #
##########

from collections import Counter

two = sum(2 in Counter(line).values() for line in lines)
three = sum(3 in Counter(line).values() for line in lines)

print("Part 1:", two * three)


##########
# Part 2 #
##########

import itertools

for line1, line2 in itertools.combinations(lines, 2):
    differences = set(enumerate(line1)) - set(enumerate(line2))
    if len(differences) == 1:
        i = differences.pop()[0]
        print("Part 2:", line1[:i] + line1[i+1:])
