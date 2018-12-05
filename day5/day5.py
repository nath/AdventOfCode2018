import re

with open('input.txt') as f:
    str = f.read().strip()

def reduce(s):
    result = ""
    i = 0
    while i < len(s) - 1:
        if s[i].lower() == s[i+1].lower() and ((s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].islower())):
            i += 2
        else:
            result += s[i]
            i += 1

    if i < len(s):
        result += s[i]

    return result

def fullyReduce(str):
    original = str
    reduced = reduce(str)

    while len(original) > len(reduced):
        original, reduced = reduced, reduce(reduced)

    return reduced

##########
# Part 1 #
##########

print("Part 1:", len(fullyReduce(str)))


##########
# Part 2 #
##########

alphabet = set(str.lower())

def reactWithoutLetter(str, c):
    s = re.sub('({}|{})'.format(c, c.upper()), '', str)
    return fullyReduce(s)

print("Part 2:", min(len(reactWithoutLetter(str, c)) for c in alphabet))
