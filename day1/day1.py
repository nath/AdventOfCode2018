with open('input.txt') as f:
    deltas = [int(x) for x in f]

##########
# Part 1 #
##########

print("Part 1:", sum(deltas))


##########
# Part 2 #
##########

import itertools

freq = 0
seen = set([0])
for delta in itertools.cycle(deltas):
    freq += delta
    if freq in seen:
        print("Part 2:", freq)
        break
    seen.add(freq) 
